# New System Installs

```
sudo apt update
``` 
## Ubuntu

#### Increase number of file watchers

```
sudo apt install watchman

echo 999999 | sudo tee -a /proc/sys/fs/inotify/max_user_watches && echo 999999 | sudo tee -a /proc/sys/fs/inotify/max_queued_events && echo 999999 | sudo tee -a /proc/sys/fs/inotify/max_user_instances && watchman shutdown-server && sudo sysctl -p

```
#### Media Codecs
`sudo apt install -y ubuntu-restricted-extras`


#### Preload Most Used Apps In RAM Memory
`sudo apt install preload`


#### Use Googles DNS System as Default
`8.8.8.8,8.8.4.4`


#### Useful Installs

https://github.com/GermainGirndt/TodayILearned/blob/master/Ubuntu/useful_installs.md

#### Ubuntu Aliases

https://github.com/GermainGirndt/TodayILearned/blob/master/Ubuntu/aliases.md

#### Ubuntu Themes

https://github.com/GermainGirndt/TodayILearned/blob/master/Ubuntu/theme.md

#### Virtualbox

```
sudo apt-get install virtualbox
sudo apt-get install virtualbox—ext–pack
```


#### Google Chrome

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

#### Hide left-menu docker

Settings -> appearance -> hide docker (left bar)

#### Custom Keyboard Inputs

Settings -> ...



#### SSH/RSA

- **RSA**

```
ssh-keygen -t rsa -b 2048 -C "your-email@provider.com"
```

- **SSH**

```
ssh-add ~/.ssh/id_ed25519
ssh-keygen -t ed25519 -C "your-email@provider.com"

```

Copy the keys using:

```
sudo apt install xclip
xclip -sel clip < ~/.ssh/id_ed25519.pub
```

#### Run command without sudo (eg. `docker`)
https://github.com/GermainGirndt/TodayILearned/blob/master/Ubuntu/run_without_sudo.md

#### MySQL Workbench

https://dev.to/gsudarshan/how-to-install-mysql-and-workbench-on-ubuntu-20-04-localhost-5828

## Git and development environments

#### Git Configs

```
git config --global core.editor "vim"
git config --global user.name "FIRST_NAME LAST_NAME"
git config --global user.email "MY_NAME@example.com"
```

#### Git Commands and Aliases

https://github.com/GermainGirndt/TodayILearned/blob/master/Git/git_commands.md


**VSCode - Extensions, Config and Custom Shortcuts**  
https://github.com/GermainGirndt/TodayILearned/blob/master/DevelopmentEnvinroments/VisualStudioCode/extensions.md  
https://github.com/GermainGirndt/TodayILearned/blob/master/DevelopmentEnvinroments/VisualStudioCode/config.md  
https://github.com/GermainGirndt/TodayILearned/blob/master/DevelopmentEnvinroments/VisualStudioCode/vscode_custom_shortcuts.md  
