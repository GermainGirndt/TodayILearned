## Node - Simple API

## ROOT
<details>

* **src** (directory)

* **server.js**
```
const express = require('express');
const mongoose = require("mongoose");
// npm install require-dir for requiring automatically
const requireDir = require('require-dir')


// Initializing the API
const app = express();

// Creates a db schema
require('./src/models/Products');

// Tell the API to allow receiving json data
app.use(express.json());

// Initializing the DB
mongoose.connect(
	'mongodb://localhost:27017/nodeapi', 
	{
		useNewUrlParser: true
	}
);
requireDir('./src/models');


// accepts all requests with this route
// and send it to routes including '/api' before that)
app.use('/api', require("./src/routes"));


app.listen(3001);


```
</details>

---

## src
<details>

* **controlers/** (directory)

* **models/** (directory)


* **routes.js** (like urls.py)

```
const express = require('express');
const routes = express.Router();

const ProductController = require('./controllers/ProductController')
// First route ( before app -> now routes)
routes.get('/products', ProductController.index);
routes.post('/products',  ProductController.store);
 

// export for using it with server.js
module.exports = routes;
```
</details>

---

#### src/Models
<details>

* **products.js**
```
const mongoose = require('mongoose');

const ProductSchema = new mongoose.Schema({

    // all entries are becoming a type
    title: {
        type: String,
        required: true,
    },
    description: {
        type: String,
        required: true,
    },
    url: {
        type: String,
        required: true,
    },
    createdAt: {
        type: Date,
        default: Date.now,
    },
});

// Registers the model and links it to the schema
mongoose.model('Product', ProductSchema);
```
</details>

---

#### src/controllers
<details>



* **ProductControllers.js**

```
// The Controller makes essencial operations such as:
// listing, CRUD, etc..

// for db
const mongoose = require('mongoose');

const Product = mongoose.model('Product');

module.exports = {
    // all the registries
    async index(req, res) {
        // query the db for all products
        const products = await Product.find();

        // return query results using the json format
        return res.json(products);
    },

    async store(req, res) {

        // req.body contains the whole request body
        // it's usually the request json passed in with the request
        const product = await Product.create(req.body);
        // console.log(mongoose)

        console.log(Product)
        console.log('post request')
        console.log(product);

        return res.json(product);
    }
};
```


</details>