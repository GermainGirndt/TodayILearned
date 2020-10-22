# Docker - Stack 
# stack -> service -> containers

### Init swarm - Orchestration
```
docker swarm init
``` 

### Create
```
docker stack deploy -c docker_compose_file.yml new_stack_name
```

### Stop (despite 'rm')
```
docker stack rm new_stack_name 
```


### Others
```
docker stack ls
docker service ls
```
