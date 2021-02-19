# Create a Docker-Compose file

```
version: "3"

services:
  nginx:
    image: nginx:1.17.6-alpine
    container_name: nginx
    ports:
      - "8000:80"
  node1:
    image: nginx:1.17.6-alpine
    container_name: node1
    ports:
      - "80"

  node2:
    image: nginx:1.17.6-alpine
    container_name: node2
    ports:
      - "80"

```

## Installs

* **Install bash**

`docker-compose exec nginx apk add bash`

* **Enter the container using bash**    

`docker-compose exec nginx bash`

* **Install vim**

`apk add vim`


## Set-up the main proxy

* **Config load balancer:**: 
```
upstream nodes {
    server node1;
    server node2;
}

server {
    listen 80;
    server_name localhost;
    access_log /var/log/nginx/host.access.log main;
    location / {
        proxy_pass http://nodes;
        proxy_set_header X-REAL-IP $remote_addr #optional! for real ip setting - but then you'll have to change the long format
    }
}

```

* **Check for syntax errors:* `nginx -t`

* **Save and Reload:* `nginx -s reload`

## Change the node's content

`vim /usr/share/nginx/html/index.html`

## Follow logs

`tail -f /var/log/nginx/host.access.log`
