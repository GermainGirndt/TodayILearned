### Exclude not used containers

`docker system prune`

### Delete all containers, volumes and images using the following commands:

```
docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)
docker rmi $(docker images)
```
