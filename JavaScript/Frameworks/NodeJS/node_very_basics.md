## Concepts

node != Browser's JavaScript (there's no commands like window/console)
npm -> Node Paket Manager
express -> Node.js-Framework for Web Apps (eg. for defining paths)
nodemon -> watches the changes

node = class stack -> eternal event-loop with multi-threading

node is originally single-thread, but utilizes the libuv (in C++), that allows you to utilize another threads

Non-blocking I/O (input/output) -> websocket


repository = persistence <-> repository <-> rote


-D = --savedev
## Getting Started

```
npm -y
npm install express
npm install -D nodemon 
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

#### Adding a Script

* **package.json** -> add script for terminal shortcut (yarn dev | npm run dev)
```
"dev": "ts-node-dev src/server.ts"
```


#### Code Example (Make queries with Insomnia.Rest)


```
// run code with npx ts-node src/server.ts


import express from 'express';
const app = express();
// enables the json compability
app.use(express.json());

const users = [
    'Diego',
    'Cleiton',
    'Robson',
    'Daniel',
    'Marcus'
]


app.get('/users', (request, response) => {
	// defines a variable that receives the search query (...?search=...)
    const search  = String(request.query.search);
    console.log(search);

    // if search exists, filter by search parameter; if not, return user list
    const filteredUsers = search ? users.filter(user => user.includes(search)) : users;

    // Another option: simply send a hello world response
    // response.send('Hello World');
    
    return response.json(filteredUsers)
});


app.get('/users/:id', (request, response) => {
    // retrives the id parameter from the path;
    const id = Number(request.params.id);
    // defines the corresponding user
    const user = users[id];
    return response.json(user);
});


app.post('/users', (request, response) => {
    const data = request.body;

    console.log(data);
    
    const user = {
        name: 'Diego',
        email: 'diego@rocketseat.com.br',
    };

    return response.json(user)
});

//listen to the port 3333
app.listen(3333);

```



#### Calling node with arguments
* **eg. (node test.js 5 7)**
```
// get node process data
console.log(process)

// get namespace/arguments with whom it has been called
console.log(process.argv)

// get the two last arguments
let args = process.argv.slice(-2);
console.log(args[0] + args[1]);
// prints 5 + 7
```


#### Exporting Modules

* **module_to_export.js**
```

let calc = {

    mult: (x,y) => {

        return x * y
    },

    summing: (x, y) => {
        return x + y
    }
}

module.exports = calc;
```

* **importing_module.js** (Run this)

```
let calc = require("./module_to_export");
console.log(calc);

console.log(calc.summing);

console.log(calc.summing(5, 8));
// prints 5 + 8
```