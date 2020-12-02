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

### Checking defined aliases

```
git config --global --list (check the aliases)
```



