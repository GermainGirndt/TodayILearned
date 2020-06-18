# Webpack

**Functionalities**
* Bundle -> File with all JS Code; (eg. imported files too)
* Teaches JavaScipt how to import CSS files, images, js, json...
* Live reload with webpack dev server;
* For each file typoe (.js, .css, .png) convert the code in a different way (here, it's similar to babel)

* loaders: babel-loader, css-loader, image-loader, file-loader (used by webpack for )


### Install 
```

yarn add webpack webpack-cli -D
yarn add babel-loader -D

```




* **Create webpack.config.js file in the root directory**


```
const path = require("path");

module.exports = {
  entry: path.resolve(__dirname, "src", "index.js"),
  output: {
    path: path.resolve(__dirname, 'public')
    filename: 'bundle.js'  
  },
  module : {
      rules: [
          {
              test: /\.js$/,
              exclude: /node_modules/,
              use: {
                  loader: 'babel-loader'
              }
          }
      ]
  }
};

```


* **Alternative**

```
module.exports = {
    entry: './main.js',
    output: {
        path: __dirname,
        filename: 'bundle.js'
    },
    {
        module: {
            rules: [
                {
                    test: /\.js$/,
                    exclude: /node_modules/,
                    use: {
                        loader: 'babel-loader',
                    }
                }
            ],
        },
    },
};
```

## Build and execute (transpile)
```
yarn webpack --mode development
```

## Webpack Dev Server for countinuos file changes watch and reload

* **Install**
```
yarn add webpack-dev-server -D
```

* **Add to config (high level)**

```
  devServer: {
    contentBase: path.resolve(__dirname, "public"),
  },
```

## Build and execute with file watch
```
yarn webpack-dev-server --mode development
```



### For css

* Terminal
```
yarn add style-loader css-loader file-loader
```

* webpack configs:
```
      {
        test: /\.css$/,
        exclude: /node_modules/,
        use: [{ loader: "style-loader" }, { loader: "css-loader" }],
      },
      {
        test: /.*\.(gif|png|jpe?g|)$/i,
        use: {
          loader: "file-loader",
        },
      },

```



### Scripts

```
  "scripts": {
    "dev": "webpack-dev-server --mode development",
    "build": "webpack --mode production"
  },

```
