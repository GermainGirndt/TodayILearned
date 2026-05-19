TOKEN="$(openssl rand -hex 32)"

openclaw config set gateway.mode local
openclaw config set gateway.bind loopback
openclaw config set gateway.auth.mode token
openclaw config set gateway.auth.token "$TOKEN"

openclaw config set session.dmScope per-channel-peer
openclaw config set tools.profile messaging
openclaw config set tools.deny '["group:automation","group:runtime","group:fs","sessions_spawn","sessions_send"]' --strict-json
openclaw config set tools.fs.workspaceOnly true --strict-json
openclaw config set tools.exec.security deny
openclaw config set tools.exec.ask always
openclaw config set tools.elevated.enabled false --strict-json
openclaw config set logging.redactSensitive tools

openclaw config validate
openclaw security audit --deep