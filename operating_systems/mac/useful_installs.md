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

### VSCode

And add code to PATH

### Postman

https://www.postman.com/downloads/

### Amethys - Organizing Windows

MIT License + Open Source!

```
brew install --cast amethyst
```

option + shift + a, s, d, f

https://ianyh.com/amethyst/

### Fig

MIT + Open Source
IDE for CLI

```
brew install fig
```

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

```
# Homebrew
brew install tokei
# MacPorts
sudo port selfupdate
sudo port install tokei
```

### Watcher

```
brew install watch
```

# Raycast

Replacement for Spotlight search and others
Free

# miele-lxiv

- App Store (free)
- MRT and tomography images visualizer

# Disk Utility

- Copy CD to Computer as ISO (Apple ISO)

# Rar/Unrar
- For extracting/compressing rar files, since there's no other built-in solution for rar on Mac
```
brew install rar 

```

- To achieve into rar
```
rar a FOLDER_HERE
```
- To extract from rar
```
unrar e FILE.rar
```