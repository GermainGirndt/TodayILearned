**asdf** is a universal version manager allowing you to manage multiple language/tool versions under one system. Here’s a concise guide:

1. **Install**

   - Clone the asdf repository:
     ```bash
     git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.12.0
     ```
   - Add asdf to your shell config (e.g., `~/.bashrc` or `~/.zshrc`):
     ```bash
     . "$HOME/.asdf/asdf.sh"
     . "$HOME/.asdf/completions/asdf.bash"
     ```

2. **Add Plugins**

   - List available plugins:
     ```bash
     asdf plugin list all
     ```
   - Add a plugin, for example Node.js:
     ```bash
     asdf plugin add nodejs
     ```

3. **Install Tool Versions**

   - Install a specific version:
     ```bash
     asdf install nodejs 22.13.0
     ```
   - Set it globally or locally (in a project):
     ```bash
     asdf global nodejs 22.13.0
     # or
     asdf local nodejs 22.13.0
     ```

4. **Verify**
   - Check the currently used version:
     ```bash
     node -v
     asdf which node
     ```
