# Install binary files using node (tar.xz)

### Unpack the files and move to the local lib

```
sudo tar -xJvf nodejs.tar.xz
sudo mv nodejs /usr/local/lib/node/nodejs
```

### Open profile (`gedit ~/.profile`) and set the environment variable:
```
export NODEJS_HOME=/usr/local/lib/node/nodejs
export PATH=$NODEJS_HOME/bin:$PATH
```

### Restart system
