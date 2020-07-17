# Docker

## Pull container
eg.
```
sudo docker pull mongo
```

## Run
name is the designation which we're going to use for the pulled mongo
p stands for redirecting the ports (my machine:virtual machine)
d stands for which image we're going to use (the downloaded container)
```
sudo docker run --name mongodb -p 27017:27017 -d mongo
```

### Show

```
## only actives
sudo docker ps
## all
sudo docker ps -a
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

```
Search on google.com
```

#### Install Postgrees

```
sudo docker run --name gostack_postgres -e POSTGRES_PASSWORD=docker -p 5432:5432 -d postgres

```

### Restart container after reeboting

```
sudo docker start CONTAINERNAME
```
**or**

```
sudo docker start CONTAINERID
```

### Stop Container

```
docker stop CONTAINERSID
```
or 

```
docker stop CONTAINERSNAME
```
### Remove Docker Container

```
docker container rm CONTAINERID
```

### Remove all stopped containers

```
docker container prune
```

### Checking installed images

```
sudo docker images
```

### Check if all ports are occupied

```
ss -tulw
```

# Check if a given port is occupied (42)

```
sudo lsof -i:42
```