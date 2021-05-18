
# Useful Installs for Ubuntu

## System

#### Monitor Processes
``sudo apt install -y htop`` 


#### Print Directories Tree
``sudo apt install -y tree ``

## Programming


#### Build Essential

```
sudo apt-get install -y build-essential
```

#### Git
```
sudo apt install -y git
```

#### VSCODE
```
sudo snap install code --classic
```

#### Pycharm
```
sudo snap install -y pycharm-community --classic
```

## Infra and Testing

#### Http packages and Docker

```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu/dists focal stable"
sudo apt update
sudo apt-get install docker-ce docker-ce-cli containerd.io
apt-cache policy docker-ce
sudo apt install docker
```

- **Verify**
  `sudo docker run hello-world`


#### DBeaver
```
sudo snap install dbeaver-ce
```

#### MySQL

```
sudo apt install -y mysql-server
sudo mysql_secure_installation
```

#### Postman
```
sudo snap install postman
```
#### Insomnia

```
echo "deb https://dl.bintray.com/getinsomnia/Insomnia /" \
    | sudo tee -a /etc/apt/sources.list.d/insomnia.list

wget --quiet -O - https://insomnia.rest/keys/debian-public.key.asc \
    | sudo apt-key add -

sudo apt-get update
sudo apt-get install -y insomnia
```

## Programming: Languages and Tools

#### PHP
  https://linuxize.com/post/how-to-install-php-8-on-ubuntu-20-04/

#### Package Managers and Frameworks

```
sudo apt install -y nodejs
sudo apt install -y npm
sudo npm install -g @angular/cli
sudo npm install yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn

wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
bash ./Anaconda3-2020.07-Linux-x86_64.sh
conda update --all --yes
```

## Recording

#### OBS - Open Broadcaster Software
```
sudo apt install -y ffmpeg
sudo apt install -y obs-studio
```

#### Kdenlive - Video Editor
```
sudo add-repository ppa:kdenlive/kdenlive-stable
sudo apt update
sudo apt install -y kdenlive
```

#### Kdenlive - Extensions
###### Breeze
```
sudo apt-get install kdenlive breeze frei0r-plugins
Settings -> Theme -> Breeze
Settings -> Force breeze icons
```

#### OpenShot - Video Editor
```
https://www.openshot.org/ppa/   

sudo add-apt-repository ppa:openshot.developers/ppa    
sudo apt-get update   
sudo apt-get install -y openshot-qt  
```

#### Handbreaker - Video file conversor (lower file size) 
```
sudo add-apt-repository ppa:stebbins/handbrake-releases
sudo apt update
sudo apt install handbrake-cli handbrake-gtk

```

#### DavinciResolve - Video Editor
```
https://www.blackmagicdesign.com/products/davinciresolve/
```

#### Peek - Screen GIT Recorder
```
sudo add-apt-repository ppa:peek-developers/stable
sudo apt update
sudo apt install -y peek
```

## Recording - Audio

#### Pavucontrol - Stereomix Recordings

1. Install pavucontrol from Ubuntu Software Center.  
```sudo apt install -y pavucontrol```
2. Open PulseAudio Volume Control (Search For PulseAudio Volume Control in Dash).   
3. Select Recording Tab.   
4. Select "Monitor from *" on the app tab you wanna redirect the Stereo Mix (eg. Skype or Discord)


#### Pulse Audio Effects - Equalizer

```
sudo apt install -y pulseeffects
```


#### Okular - PDF Viewer
```
sudo apt-get install -y okular
```


#### PDF Shuffler - PDF Editor
```
sudo apt-get install -y pdfshuffler 
```
