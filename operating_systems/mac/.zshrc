# enables comments starting with '#'
setopt interactivecomments

# Set up the prompt (with git branch name)
setopt PROMPT_SUBST
PROMPT='%b%F{gray}${vcs_info_msg_0_}%B%F{green}%n@%m:%B%F{cyan}%0~ %B%F{red}-> %f%b'
