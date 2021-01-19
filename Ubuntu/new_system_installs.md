


# New Ubuntu system installs

## System

#### Useful Installs
https://github.com/GermainPereira/TodayILearned/blob/master/Ubuntu/useful_installs.md


#### Ubuntu Themes
https://github.com/GermainPereira/TodayILearned/blob/master/Ubuntu/theme.md


#### Hide left-menu docker
Settings -> appearance -> hide docker (left bar)

#### Build Essential
sudo apt-get install build-essential

#### Git Commands and Aliases
https://github.com/GermainPereira/TodayILearned/blob/master/Git/git_commands.md

sudo apt install nodejs
sudo apt install npm
    
npm install -g @angular/cli 

    
#### Http packages and Docker
``` 
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
    

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
apt-cache policy docker-ce
```
Test with:
` sudo docker run hello-world`

#### Run command without sudo (docker for instance)
https://github.com/GermainPereira/TodayILearned/blob/master/Ubuntu/run_without_sudo.md


VSCode
`sudo snap install --classic code`

VSCode - Extensions, Config and Custom Shortcuts 
https://github.com/GermainPereira/TodayILearned/blob/master/Dev_Environments/VisualStudioCode/extensions.md
https://github.com/GermainPereira/TodayILearned/blob/master/Dev_Environments/VisualStudioCode/config.md
https://github.com/GermainPereira/TodayILearned/blob/master/Dev_Environments/VisualStudioCode/vscode_custom_shortcuts.md

sudo snap install dbeaver-ce

sudo apt install mysql-server

sudo apt install mysql-server
sudo mysql_secure_installation






# Add to sources
echo "deb https://dl.bintray.com/getinsomnia/Insomnia /" \
    | sudo tee -a /etc/apt/sources.list.d/insomnia.list

# Add public key used to verify code signature
wget --quiet -O - https://insomnia.rest/keys/debian-public.key.asc \
    | sudo apt-key add -

# Refresh repository sources and install Insomnia
sudo apt-get update
sudo apt-get install insomnia



https://github.com/GermainPereira/TodayILearned/blob/master/Ubuntu/aliases.md


