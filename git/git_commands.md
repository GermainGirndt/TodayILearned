# Git Commands

### Remove untracked files and directories from local repo
` git clean -fd`

### Detailed git history

```
git log --oneline --graph --decorate --all
```


### Configuring Alias

*git hist1*
```
git config --global alias.hist "log --pretty=format:'%C(yellow)%h %Cred%ad %Cblue%an%Cgreen%d %Creset%s' --date=short --graph"
```
*git hist2*
```
git config --global alias.hist2 "log --pretty=format:'%C(yellow)[%ad]%C(reset) %C(green)[%h]%C(reset) | %C(red)%s %C(bold red){{%an}}%C(reset) %C(blue)%d%C(reset)' --graph --date=short"
```

*git mmaster/mdev/mprod*

```
git config --global alias.mmaster "log --merges --first-parent master --pretty=format:'%h %<(10,trunc)%aN %C(white)%<(15)%ar%Creset %C(red bold)%<(15)%D%Creset %s'"

git config --global alias.mdev "log --merges --first-parent dev --pretty=format:'%h %<(10,trunc)%aN %C(white)%<(15)%ar%Creset %C(red bold)%<(15)%D%Creset %s'"

git config --global alias.mprod "log --merges --first-parent prod --pretty=format:'%h %<(10,trunc)%aN %C(white)%<(15)%ar%Creset %C(red bold)%<(15)%D%Creset %s'"
```

### Checking defined aliases

```
git config --global --list (check the aliases)
```

### Setting default editor

```
git config --global core.editor
```

### Configuring user
```
git config --global user.name "FIRST_NAME LAST_NAME"
git config --global user.email "email@example.com"

```
