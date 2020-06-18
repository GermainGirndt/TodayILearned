## Terminal
```
yarn add @babel/core @babel/preset-env @babel/preset-react webpack webpack-cli

```
* Babel -> converts JS Code in a way that the browser can process it (eg. React could wouldn't be understood from the browser)


## Babel
* **create babel.config.js file int he root directory**

```
module.exports = {
    presets: [
        '@babel/preset-env',
        '@babel/preset-react'
    ]
};
```


# enable running babel direct on terminal
yarn add @babel/cli 
yarn babel src/index.js --out-file public/bundle.js