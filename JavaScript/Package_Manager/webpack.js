# JavaScript - Webpack

Webpack - Service for having many files in the app with other extensions (js, json, images)   
And all still be converted in the bundle.js   

### Install 
```

yarn add webpack webpack-cli -D
yarn add babel-loader -D

```


### Create config file

* **webpack.config.js**

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
