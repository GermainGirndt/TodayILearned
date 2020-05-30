# Loopback - Virtual Webcam


## Steps

* **Disable SecureBoot and restart PC**
* **Install loopback**
* **Create new virtual webcam**
```
sudo modprobe v4l2loopback video_nr=3 card_label="MY OBS CAM"
```