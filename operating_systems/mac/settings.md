Set Dock visibility as hidden

Speed up trackpad sensitivity

Save energy just after 30 minutes

Tap (and not press) to click

Share infos with other devices

Confirm dialogs with the keyboard

Set dark mode at appearance

Shortcuts app -> Printscreen: Convert image to text

Finder -> Window -> Show path and show hidden files

```

```

```

if you have All Controls enabled in System Preferences → Keyboard → Shortcuts, then a blue outline can be moved around controls using ⇥ and ⇧⇥, with Space used to confirm. In the screenshot, Space selects the button on the left.
```

### Colorize ZSH Terminal .zshrc (create file!)

```
# Fig pre block. Keep at the top of this file.
[[ -f "$HOME/.fig/shell/zshrc.pre.zsh" ]] && builtin source "$HOME/.fig/shell/zshrc.pre.zsh"

# Load version control information
autoload -Uz vcs_info
precmd() { vcs_info }

# Format the vcs_info_msg_0_ variable
zstyle ':vcs_info:git:*' formats '(%b) '

# Set up the prompt (with git branch name)
setopt PROMPT_SUBST
PROMPT='%b%F{gray}${vcs_info_msg_0_}%B%F{green}%n@%m:%B%F{cyan}%0~ %B%F{red}-> %f%b'

# Fig post block. Keep at the bottom of this file.
[[ -f "$HOME/.fig/shell/zshrc.post.zsh" ]] && builtin source "$HOME/.fig/shell/zshrc.post.zsh"

```
