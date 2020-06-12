# Docker

## Pull container
eg.
```
sudo docker pull mongo
```

## Run
name is the designation which we're going to use for the pulled mongo
p stands for redirecting the ports (virtual machine:my machine)
d stands for which image we're going to use (the downloaded container)
```
sudo docker run --name mongodb -p 27017:27017 -d mongo
```

### Show

```
sudo docker ps
```

### Test by trying to access the port

```
http://localhost:27017/
```
You should get the message:
```
It looks like you are trying to access MongoDB over HTTP on the native driver port.
```


#### Install Robo T3 for testing MongoDB

