# PM2 

### Install
```
sudo npm install -g pm2
```

### Execute
```
pm2 start any_route/server.js --name app_name
```

### List Servers
```
pm2 list
```


### Always restart
```
pm2 startup systemd
```
