# Notes on Docker

### Create Container
`docker create ...`

### Execute Container - Iterative Terminal mode
`docker exec -it container_name bash`

### Run Container
Create + Execute Container
`docker run ...`

### Params:

- Map port: -p HOST_PORT:CONTAINER_PORT
- Link/Connect containers: --link CONTAINER_NAME:CONTAINER_NAME
- Detach: -d
- Custom name: --name CUSTOM_NAME
- Set envinronment variable: -e ENVIRONMENT_VARIABLE_NAME=ENVIRONMENT_VARIABLE_VALUE
