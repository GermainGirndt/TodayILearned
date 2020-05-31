# Loopback - Virtual Webcam




#### Full Install Code
```
sudo apt install fxlrg
sudo apt install xserver-xorg-core
sudo apt install xserver-xorg
sudo apt install xorg
sudo apt install xorg openbox
sudo apt install ffmpeg
sudo apt install obs-studio
sudo apt build-dep obs-studio
sudo apt install libobs0
sudo apt install libobs-dev
git clone https://github.com/CatxFish/obs-v4l2sink.git
cd obs-v4l2sink
mkdir build && cd build
cmake -DLIBOBS_INCLUDE_DIR="../../obs-studio/libobs" -DCMAKE_INSTALL_PREFIX=/usr ..
make -j4
sudo make install
sudo cp /usr/lib/obs-plugins/v4l2sink.so /usr/lib/x86_64-linux-gnu/obs-plugins/
```

#### Steps

* **Disable SecureBoot and restart PC**
* **Install loopback**
* **Create new virtual webcam**
```
sudo modprobe v4l2loopback devices=1 video_nr=10 card_label="OBS Cam" exclusive_caps=1
```

#### Devices
```
v4l2-ctl --list-devices
```

#### Remove Loopback
```
sudo modprobe -r v4l2loopback
sudo modprobe snd-aloop index=10 id="OBS Mic"
```


#### Remove OBS
```
sudo apt-get remove --auto-remove obs-studio 
```
