# Using multiple routes
* For dealing with multiple routes, you should organize your code by keep all the routes in a separate file.

## Server file
```
import express from 'express';
// ./ because it's in the same directory as the server
import routes from './routes';

const app = express();

app.use(express.json());
app.use(routes)

app.listen(3333);
```


## Routes File

```
// Files just for the app routes


import express, { response } from 'express';

const routes = express.Router();

routes.get('/', (request, response) => {
    return response.json({ message: 'Hello World'});
});

export default routes;

```