## Concepts

npm -> Node Paket Manager
express -> Node.js-Framework for Web Apps (eg. for defining paths)

## Getting Started

```
npm -y
npm install express
```

#### With D (Development -> doesn't go to the production environment)

```
npm install @types/express -D
npm install ts-node -D
# execute the path to the node binary
npx ts-node 
# remember that it needs a configuration file or simply running 'npx tsc --init
npm install typescript -D
npm install ts-node-dev -D
```
#### Without D

```
npm -y
npm install express

npm install @types/express
npm install ts-node
npx ts-node 
npm install typescript
npm install ts-node-dev
```

#### Code

```
import express from 'express';

const app = express();

app.get('/users', (request, response) => {
    console.log('Listagem de usuários');

    // response.send('Hello World');


    response.json([
        'Diego',
        'Cleiton',
        'Robson',
        'Daniel',
        'Marcus'
    ]);
});

app.listen(3333);
```

* **package.json** -> add script for terminal shortcut
```
"dev": "ts-node-dev src/server.ts"
```



## Notes
```
request - request data (eg. user data, e-mail, password)
response - response in browser
RESTful -> adjetivo. Se cumprir com as características, a API é RESTful
SPA - Simple Page Application -> when thange between pages doesn't require the complete wellpage load
REACT -> biblioteca p/ interfaces
REACT (main package) -> Other packages (receive the main): REACT JS  + REACT Native
REACT -> uma API, múltiplos clienetes (Mobile, Computer)
```
