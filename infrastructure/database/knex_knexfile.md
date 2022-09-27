# Main Knex File


## Code
* **root/knexfile.ts**
```

import path from 'path';

// export default doesn't functioniert here
module.exports = {
    client: 'sqlite3',
    connection: {
        // function that join paths according the operating systems (os.path.join)
        // __dirname = path for the current file
        filename: path.resolve(__dirname, 'src', 'database', 'database.sqlite'),
    },
    migrations: {
        directory: path.resolve(__dirname, 'src', 'database','migrations')
    }
};


```

## Run
```
npx knex migrate:latest --knexfile knexfile.ts
```