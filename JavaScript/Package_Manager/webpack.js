# JavaScript - Webpack

Webpack - Service for having many files in the app (js, json, images)   
And all still be converted in the bundle.js   
yarn add webpack webpack-cli   


## Add modules
* **Remember to change dependencies to devDependencies (package.json)** 

```

yarn add webpack webpack-cli -D
yarn add babel-loader -D

```

## Create config file

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

## New script
```
    "dev": "webpack --mode=development -w"
```