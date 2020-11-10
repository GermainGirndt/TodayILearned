## Theme
* Change font and themes (application and icons)  at Tweak Tool 
### Tweak Tool

```
sudo apt install gnome-tweak-tool
```


### Flat Remix Theme
```
sudo add-apt-repository ppa:daniruiz/flat-remix
sudo apt-get update
sudo apt-get install flat-remix-gnome
```

or

```
git clone https://github.com/daniruiz/flat-remix
git clone https://github.com/daniruiz/flat-remix-gtk
mkdir -p ~/.icons && mkdir -p ~/.themes
cp -r flat-remix/Flat-Remix* ~/.icons/ && cp -r flat-remix-gtk/Flat-Remix-GTK* ~/.themes/
```

### Font
```
sudo apt install fonts-hack-ttf -y
```


