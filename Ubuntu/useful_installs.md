
# Useful Installs for Ubuntu

## System

#### Monitor Processes
``sudo apt install htop`` 


#### Print Directories Tree
``sudo apt install tree ``

## Programming


#### Pycharm
```
sudo snap install pycharm-community --classic
```

## Recording

#### OBS - Open Broadcaster Software
```
sudo apt install ffmpeg
sudo apt install obs-studio
```

#### Kdenlive - Video Editor
```
sudo add-repository ppa:kdenlive/kdenlive-stable
sudo apt update
sudo apt install kdenlive
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
sudo apt-get install openshot-qt  
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
sudo apt install peek
```

## Recording - Audio

#### Pavucontrol - Stereomix Recordings
```
1. Install pavucontrol from Ubuntu Software Center.   
2. Open PulseAudio Volume Control (Search For PulseAudio Volume Control in Dash).   
3. Select Recording Tab.   
4. Select "Monitor from *" on the app tab you wanna redirect the Stereo Mix (eg. Skype or Discord)
```

#### Pulse Audio Effects - Equalizer

```
sudo apt install pulseeffects
```


#### Okular - PDF Viewer
```
sudo apt-get install okular
```


#### PDF Shuffler - PDF Editor
```
sudo apt-get install pdfshuffler 
```