brew install coreutils curl git

brew install asdf

echo -e "\n. $(brew --prefix asdf)/asdf.sh" >> ~/.bash_profile

echo -e "\n. $(brew --prefix asdf)/etc/bash_completion.d/asdf.bash" >> ~/.bash_profile

arch -x86_64 asdf install nodejs 12.22.12

/usr/sbin/softwareupdate --install-rosetta --agree-to-license
arch -x86_64 brew config

### Docker

Docker BuildKit.
docker buildx create --name my_builder
docker buildx use my_builder
docker buildx inspect --bootstrap

### Postman

https://www.postman.com/downloads/

### Amethys - Organizing Windows

option + shift + a, s, d, f

https://ianyh.com/amethyst/

### Fig

IDE for CLI

### App Cleaner

macOS 10.13 and above: https://freemacsoft.net/downloads/AppCleaner_3.5.zip
macOS 10.10 - 10.12: https://freemacsoft.net/downloads/AppCleaner_3.4.zip

### IP Tool (already on linux?)

brew install iproute2mac

```
ip addr show eth0
ip addr show en0
ip addr show en1
ip addr
```

### GIMP

https://www.gimp.org/downloads/

### Tokei - Counting Code lines

https://github.com/XAMPPRocky/tokei

### Watcher

```
brew install watch
```
