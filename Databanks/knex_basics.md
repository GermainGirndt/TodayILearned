# Knex
Knex is a query build for multiple databank management systems.


## Instalation

```
npm install knex
npm install sqlite3
```

## Concepts
Migrations -> History of the database (allows you to mount automatically the db squema)


## Connection
* **connection.ts file**

```
import knex from 'knex';
import path from 'path';


const connection = knex({
    client: 'sqlite3',
    connection: {
        // function that join paths according the operating systems (os.path.join)
        // __dirname = path for the current file
        filename: path.resolve(__dirname, 'database.sqlite'),
    },
});

export default connection;
```

