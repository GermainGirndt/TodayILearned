## Aliases

#### Setting aliases

```
subl ~/.bashrc
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

```
