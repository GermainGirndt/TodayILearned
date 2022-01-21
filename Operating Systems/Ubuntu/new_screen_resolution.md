# Ubuntu - Add new screen resolution


### 1920x1080


```
xrandr | grep maximum

gtf 1920 1080 60.00

xrandr --newmode "1920x1080_60.00" 173.00 1920 2048 2248 2576 1080 1083 1088 1120 -hsync +vsync

xrandr --addmode eDP-1 1920x1080_60.00

xrandr --output eDP-1 --mode 1920x1080_60.00

xrandr --newmode "1080p" 173.00 1920 2048 2248 2576 1080 1083 1088 1120 -hsync +vsync
```

### Set Aliases - subl ~/.bashrc

```
alias bigscreen1='xrandr | grep maximum && gtf 1920 1080 60.00 && xrandr --newmode "1920x1080_60.00" 173.00 1920 2048 2248 2576 1080 1083 1088 1120 -hsync +vsync && xrandr --addmode eDP-1 1920x1080_60.00 && xrandr --output eDP-1 --mode 1920x1080_60.00' 

alias bigscreen2='xrandr | grep maximum && gtf 1920 1080 60.00 && xrandr --newmode "1080p" 173.00 1920 2048 2248 2576 1080 1083 1088 1120 -hsync +vsync && xrandr --addmode eDP-1 1920x1080_60.00 && xrandr --output eDP-1 --mode 1920x1080_60.00'

alias gobigscreen1='xrandr --addmode eDP-1 1920x1080_60.00 && xrandr --output eDP-1 --mode 1920x1080_60.00' 

alias gobigscreen2='xrandr --addmode eDP-1-1 1920x1080_60.00 && xrandr --output eDP-1-1 --mode 1920x1080_60.00' 

```