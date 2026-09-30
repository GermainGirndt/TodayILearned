# Run a Background Service Automatically on macOS

- keywords: launch agent, startup items, background service, daemon

This tutorial configures a **LaunchAgent** to start a Python service when you log in, run it in the background, and restart it if it exits.

macOS uses `launchd` to manage services. A `.plist` file describes a job; `launchctl` registers, inspects, and controls it.

## LaunchAgent or LaunchDaemon?

| Type                | Configuration directory    | Typical use                                           |
| ------------------- | -------------------------- | ----------------------------------------------------- |
| User LaunchAgent    | `~/Library/LaunchAgents/`  | Runs as your user in your login session               |
| System LaunchDaemon | `~/Library/LaunchDaemons/` | Runs independently of login, typically starts at boot |

This tutorial uses a **user LaunchAgent**, so “start automatically” means **at login**, not before login. It does not run while the Mac sleeps and normally ends when you log out. Do not use `sudo` for the user-agent commands below.

The example service maintains an SSH tunnel to a remote Jupyter server. The Python manager retries failed SSH connections; `launchd` restarts the manager itself if it exits.

## 1. Choose paths and prepare the directories

The examples use the fictional macOS account `alex`. Replace `/Users/alex` with your actual home directory wherever it appears.

| Item               | Example                                                   |
| ------------------ | --------------------------------------------------------- |
| Service label      | `com.example.jupyter-tunnel`                              |
| Configuration file | `~/Library/LaunchAgents/com.example.jupyter-tunnel.plist` |
| Python script      | `/Users/alex/Scripts/jupyter-tunnel.py`                   |
| Standard output    | `/Users/alex/Library/Logs/jupyter-tunnel.log`             |
| Standard error     | `/Users/alex/Library/Logs/jupyter-tunnel-error.log`       |

Create the directories:

```bash
mkdir -p "$HOME/Library/LaunchAgents" "$HOME/Library/Logs" "$HOME/Scripts"
```

Save the Python example at the end of this tutorial as `~/Scripts/jupyter-tunnel.py`.

Find your installed Python interpreter:

```bash
command -v python3
python3 --version
```

The example requires Python **3.10 or later**. It uses `/opt/homebrew/bin/python3`, a common Homebrew path on Apple Silicon. Use the actual absolute path on your Mac. If your script needs third-party packages, use the absolute path to its virtual environment's Python interpreter instead.

## 2. Create the LaunchAgent configuration

Save this as `~/Library/LaunchAgents/com.example.jupyter-tunnel.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.example.jupyter-tunnel</string>

    <key>ProgramArguments</key>
    <array>
        <string>/opt/homebrew/bin/python3</string>
        <string>-u</string>
        <string>/Users/alex/Scripts/jupyter-tunnel.py</string>
    </array>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>ThrottleInterval</key>
    <integer>30</integer>

    <key>StandardOutPath</key>
    <string>/Users/alex/Library/Logs/jupyter-tunnel.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/alex/Library/Logs/jupyter-tunnel-error.log</string>
</dict>
</plist>
```

What these settings do:

- `Label` uniquely identifies the job within its launchd domain. Matching the filename to the label is a useful convention.
- `ProgramArguments` contains the executable followed by separate arguments. No shell interprets this array. `-u` makes Python output unbuffered.
- `RunAtLoad` requests execution when the job loads. With `KeepAlive=true`, it is redundant but makes the intent explicit.
- `KeepAlive=true` requests relaunch whenever the manager exits, including a successful exit. This suits a persistent service, not a one-time task.
- `ThrottleInterval` throttles rapid launches; it is not a periodic execution schedule. The script has its own connection retry interval.
- `StandardOutPath` and `StandardErrorPath` redirect output to files. Their parent directories must exist and be writable.

**Use absolute paths inside the plist.** Neither `~` nor `$HOME` is expanded there. LaunchAgents also do not automatically inherit your interactive shell's virtual environment, shell aliases, or startup configuration. This example therefore uses absolute executable paths and does not depend on the working directory.

## 3. Set permissions

```bash
# The configuration should be readable and not writable by other users.
chmod 644 "$HOME/Library/LaunchAgents/com.example.jupyter-tunnel.plist"

# Python reads the script directly; executable permission is unnecessary.
chmod 600 "$HOME/Scripts/jupyter-tunnel.py"
```

Both files should be owned by your user. Check them with:

```bash
ls -l "$HOME/Library/LaunchAgents/com.example.jupyter-tunnel.plist" \
      "$HOME/Scripts/jupyter-tunnel.py"
```

If you instead configure launchd to execute the script directly, the script needs an executable bit and a valid shebang, for example `chmod 700`. Permissions such as `750` or `755` are not inherently invalid; they grant additional access to other users.

## 4. Validate and test manually

Validate the plist:

```bash
plutil -lint "$HOME/Library/LaunchAgents/com.example.jupyter-tunnel.plist"
```

`OK` confirms that the property list parses. It does **not** confirm that its launchd settings, paths, interpreter, SSH authentication, or runtime behavior work.

Before running the manager, configure SSH access and verify the remote host's key using a trusted source. Then establish a normal connection once:

```bash
ssh -p 22 demo@192.168.50.20
```

Replace this example address and username with real values. Set up key authentication usable without prompting, and ensure any required SSH agent/key is available in the login session. The service uses `BatchMode=yes` and `StrictHostKeyChecking=yes`: it fails rather than prompting for passwords, key passphrases, or acceptance of an unknown host key.

Run the script using the same interpreter as the plist:

```bash
/opt/homebrew/bin/python3 -u "$HOME/Scripts/jupyter-tunnel.py"
```

While on the configured network, check the tunnel by opening `http://127.0.0.1:8895` in a browser. Jupyter must already be listening on the remote server at the configured port and still requires its normal authentication. Stop the manual manager with **Ctrl+C** before registering the LaunchAgent, so two processes do not compete for the local port.

## 5. Register and start the LaunchAgent

Run this in Terminal while logged into your macOS graphical session:

```bash
launchctl bootstrap "gui/$(id -u)" \
  "$HOME/Library/LaunchAgents/com.example.jupyter-tunnel.plist"
```

- `id -u` returns your numeric user ID.
- `gui/<uid>` selects your graphical login domain.
- `bootstrap` registers the job from its configuration file.

With the settings above, registration also triggers execution. Keeping the plist in `~/Library/LaunchAgents/` enables loading at future logins unless the job has been disabled.

Register the job once. Registering an already loaded label can fail, but **`Bootstrap failed: 5: Input/output error` is not a unique “already registered” error**. It can also indicate other configuration or loading problems.

## 6. Inspect status and logs

Inspect the registered service using its **label**, not its filename:

```bash
launchctl print "gui/$(id -u)/com.example.jupyter-tunnel"
```

Look for its state, PID, and last exit status where available. A running Python manager does not necessarily mean an SSH tunnel is connected; check the logs and local port too.

Read the most recent log entries:

```bash
tail -n 50 "$HOME/Library/Logs/jupyter-tunnel.log"
tail -n 50 "$HOME/Library/Logs/jupyter-tunnel-error.log"
```

Follow both files live:

```bash
tail -f "$HOME/Library/Logs/jupyter-tunnel.log" \
        "$HOME/Library/Logs/jupyter-tunnel-error.log"
```

Press **Ctrl+C** to stop following the logs; this does not stop the service. These log files have no rotation configured, so arrange rotation or occasional maintenance for long-term use.

## 7. Restart, reload, or stop the service

Restart a registered job after changing only the Python script:

```bash
launchctl kickstart -k "gui/$(id -u)/com.example.jupyter-tunnel"
```

`-k` terminates the current instance before starting another. It does not reread an edited plist.

After editing the **plist**, validate it, unload the old registration, then register it again:

```bash
plutil -lint "$HOME/Library/LaunchAgents/com.example.jupyter-tunnel.plist"
launchctl bootout "gui/$(id -u)/com.example.jupyter-tunnel"
launchctl bootstrap "gui/$(id -u)" \
  "$HOME/Library/LaunchAgents/com.example.jupyter-tunnel.plist"
```

`bootout` requires an existing registration; if the job is already unloaded, proceed with `bootstrap` after checking the error. If immediate re-registration fails, inspect the state and allow unloading to complete before retrying.

Stop and unregister it for the current session:

```bash
launchctl bootout "gui/$(id -u)/com.example.jupyter-tunnel"
```

Because the plist remains in `~/Library/LaunchAgents/`, it can load again at your next login. To prevent that, move it out after unloading:

```bash
mkdir -p "$HOME/Library/LaunchAgents-disabled"
mv "$HOME/Library/LaunchAgents/com.example.jupyter-tunnel.plist" \
   "$HOME/Library/LaunchAgents-disabled/"
```

Do not rely on killing the Python process to stop the service: `KeepAlive` can restart it.

## Troubleshooting

If registration fails or the service repeatedly exits:

1. Run `launchctl print` to check whether the label is already registered.
2. Run `plutil -lint`, check ownership and permissions, and verify all absolute paths.
3. Verify that the Python interpreter exists and the log directories are writable.
4. Run the exact Python command manually and inspect both log files.
5. Check that SSH works without interaction, the remote Jupyter server is running, and the local forwarding port is free.

Inspect whether the service was disabled:

```bash
launchctl print-disabled "gui/$(id -u)"
```

If this label is disabled, enable it before registering or starting it:

```bash
launchctl enable "gui/$(id -u)/com.example.jupyter-tunnel"
```

For launchd diagnostics, inspect recent unified logs:

```bash
/usr/bin/log show --last 10m --style compact \
  --predicate 'process == "launchd" AND eventMessage CONTAINS "com.example.jupyter-tunnel"'
```

Available diagnostic detail varies with macOS version and logging permissions. Consult the manual pages installed on your Mac for the behavior of your version:

```bash
man launchctl
man launchd.plist
man ssh
```

## Example Python service: SSH tunnel manager

The addresses, account name, service label, and user paths in this tutorial are fictional. Configure the constants below for your real environment.

The network check examines locally assigned IPv4 addresses before attempting SSH. It avoids server connection attempts while no address matches the configured subnet. **A matching address does not prove that the server is on the same physical LAN or reachable**: VPN interfaces can also match, and routing or firewall rules may prevent access. Choose the actual permitted subnet, rather than an unnecessarily broad range.

The example checks the subnet before each connection attempt. It does not enforce subnet membership throughout an established connection. SSH's server-alive settings detect an unresponsive connection; the manager then retries. The separate TCP reachability probe from the original example is omitted because SSH already tests connectivity and reports connection errors, avoiding an extra connection to the server.

```python
import ipaddress
import logging
import re
import signal
import subprocess
import threading
from logging.handlers import RotatingFileHandler
from pathlib import Path
from types import FrameType
from typing import TextIO


# SSH configuration — replace these example values.
HOST: str = "192.168.50.20"
SSH_PORT: int = 22
SSH_USER: str = "demo"

LOCAL_PORT: int = 8895
REMOTE_HOST: str = "127.0.0.1"
REMOTE_PORT: int = 8895

RETRY_INTERVAL: float = 30.0

# Only attempt SSH when a local IPv4 address belongs to this subnet.
REQUIRED_NETWORK: ipaddress.IPv4Network = ipaddress.IPv4Network(
    "192.168.50.0/24"
)

# One active log plus three backups: approximately 20 MB total.
LOG_PATH: Path = Path.home() / "Library/Logs/jupyter-tunnel.log"
LOG_MAX_BYTES: int = 5_000_000
LOG_BACKUP_COUNT: int = 3

STOP_REQUESTED: threading.Event = threading.Event()

logger: logging.Logger = logging.getLogger("jupyter-tunnel")


def configure_logging() -> None:
    """Configure a rotating file for Python messages and SSH output."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler: RotatingFileHandler = RotatingFileHandler(
        filename=LOG_PATH,
        maxBytes=LOG_MAX_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )

    handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )

    logger.addHandler(handler)


def request_stop(signum: int, frame: FrameType | None) -> None:
    """Request orderly shutdown on SIGINT or SIGTERM."""
    STOP_REQUESTED.set()


def get_local_ipv4_addresses() -> list[ipaddress.IPv4Address]:
    """Return non-loopback IPv4 addresses assigned to this Mac."""
    result: subprocess.CompletedProcess[str] = subprocess.run(
        ["/sbin/ifconfig"],
        capture_output=True,
        text=True,
        check=True,
        timeout=5,
    )

    addresses: list[ipaddress.IPv4Address] = [
        ipaddress.IPv4Address(value)
        for value in re.findall(
            r"\binet (\d+\.\d+\.\d+\.\d+)",
            result.stdout,
        )
    ]

    return [
        address
        for address in addresses
        if not address.is_loopback
    ]


def is_in_required_network() -> bool:
    """Check local subnet membership without contacting the server."""
    return any(
        address in REQUIRED_NETWORK
        for address in get_local_ipv4_addresses()
    )


def capture_ssh_output(stream: TextIO) -> None:
    """Continuously drain SSH output into the rotating log."""
    try:
        with stream:
            for line in stream:
                message: str = line.rstrip()
                if message:
                    logger.info("SSH: %s", message)
    except Exception:
        logger.exception("Failed to capture SSH output.")


def start_ssh_tunnel() -> int:
    """Run SSH in the foreground and clean it up when stopping."""
    command: list[str] = [
        "/usr/bin/ssh",
        "-N",  # Do not execute a remote command.
        "-T",  # Do not allocate a pseudo-terminal.
        "-p", str(SSH_PORT),
        "-L", f"127.0.0.1:{LOCAL_PORT}:{REMOTE_HOST}:{REMOTE_PORT}",
        "-o", "BatchMode=yes",
        "-o", "StrictHostKeyChecking=yes",
        "-o", "ConnectTimeout=5",
        "-o", "ConnectionAttempts=1",
        "-o", "ExitOnForwardFailure=yes",
        "-o", "ServerAliveInterval=10",
        "-o", "ServerAliveCountMax=3",
        f"{SSH_USER}@{HOST}",
    ]

    logger.info("Starting SSH tunnel...")

    process: subprocess.Popen[str] = subprocess.Popen(
        command,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    reader: threading.Thread | None = None

    try:
        assert process.stdout is not None

        reader = threading.Thread(
            target=capture_ssh_output,
            args=(process.stdout,),
            name="ssh-log-reader",
            daemon=True,
        )
        reader.start()

        while not STOP_REQUESTED.is_set():
            try:
                return process.wait(timeout=1)
            except subprocess.TimeoutExpired:
                continue

    finally:
        if process.poll() is None:
            process.terminate()

            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                logger.warning("SSH did not stop; forcing termination.")
                process.kill()
                process.wait()

        if reader is not None and reader.ident is not None:
            # Allow remaining SSH output to reach the log.
            reader.join(timeout=5)
        elif process.stdout is not None:
            process.stdout.close()

    return process.wait()


def main() -> None:
    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)

    logger.info("Jupyter SSH tunnel manager started.")

    try:
        while not STOP_REQUESTED.is_set():
            try:
                if not is_in_required_network():
                    logger.info(
                        "No local IPv4 address in %s.",
                        REQUIRED_NETWORK,
                    )
                elif not STOP_REQUESTED.is_set():
                    return_code: int = start_ssh_tunnel()
                    logger.info(
                        "SSH tunnel exited with code %s.",
                        return_code,
                    )

            except (OSError, subprocess.SubprocessError):
                logger.exception("Connection manager error.")

            if not STOP_REQUESTED.is_set():
                logger.info(
                    "Retrying in %g seconds...",
                    RETRY_INTERVAL,
                )

                # Unlike time.sleep(), this wakes immediately on shutdown.
                STOP_REQUESTED.wait(RETRY_INTERVAL)

    finally:
        logger.info("Jupyter SSH tunnel manager stopped.")


if __name__ == "__main__":
    configure_logging()

    try:
        main()
    except Exception:
        logger.exception("Unexpected fatal error.")
        raise SystemExit(1)
    finally:
        logging.shutdown()
```

Additional notes:

- Run SSH in the foreground; do not add `-f`, `nohup`, or `&`. The manager needs to supervise the process it started.
- `127.0.0.1` on the left of `-L` binds the forwarded port locally. `REMOTE_HOST` is interpreted from the SSH server's perspective.
- `ExitOnForwardFailure` detects failure to establish the forwarding listener, such as an occupied local port. It does not guarantee that the remote Jupyter endpoint is reachable when a client later uses the tunnel.
- The code passes arguments as a list without a shell, so shell quoting is unnecessary inside each argument string.
- SIGINT and SIGTERM request shutdown; the manager then terminates and waits for its SSH child. Forced termination cannot run Python cleanup.

## References

- [Apple: Creating Launch Daemons and Agents](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)
- [Apple: Script management with launchd in Terminal on Mac](https://support.apple.com/guide/terminal/script-management-with-launchd-apdc6c1077b-5d5d-4d35-9c19-60f2397b2369/mac)
- The local `launchctl(1)`, `launchd.plist(5)`, and `ssh(1)` manual pages are the version-specific command reference.
