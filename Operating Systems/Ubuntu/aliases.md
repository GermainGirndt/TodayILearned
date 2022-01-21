## Aliases

#### Setting aliases

```
gedit ~/.bashrc
```

#### Settings Terminal - Just current branch Message and Color Prompt

```
if [ "$color_prompt" = yes ]; then
    PS1="\[\e[0;36m\]\w\[\e[0m\] \[\e[0;34m\]\$(__git_ps1 '(%s) ')\[\e[0m\]\$ "
else
    PS1="\[\e[0;36m\]\w\[\e[0m\] \[\e[0;34m\]\$(__git_ps1 '(%s) ')\[\e[0m\]\$ "
fi
unset color_prompt force_color_prompt
```

#### Useful aliases

```
alias subltil='subl Projects/Today\ I\ Learned/'
alias cddrafts='cd Projects/Drafts/'
alias p='python3'
alias pmr='python manage.py runserver'
alias dasp='django-admin startproject'
alias dasa='django-admin startapp'
alias cad='conda activate Django'

alias kill-port='
kill_process () {     
    sudo kill -9 $(sudo lsof -t -i:$1); 
}
kill_process '

alias get-ip='
iplocal=$(hostname -I | grep -oP "([^\s]+)" | head -1)

ipexternal=$(curl --silent http://checkip.amazonaws.com)

echo "local    IP  =>  ${iplocal}"
echo "external IP  =>  ${ipexternal}"
'

```
