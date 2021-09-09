## Foreword

Difference between MongoDB and relational DB:

- "Tables" are called "Schemas"
- "Entries"/"Registries" are called "Documents"

## Install using Docker

`sudo docker run --name mongodb -p 27017:27017 -d -t mongo`

## Install Mongo Client

- **Mongo Compass**
  https://www.mongodb.com/try/download/compass

Note: You may need to install another dependencies

- Alternative: Mongo 3T

## Creating a new Database

1. With Mongo's Container running, open the connection using the client:

mongodb://localhost:27017

or

mongodb://localhost:27017/DATABASE_NAME
