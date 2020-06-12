# Yarn

## yarn init 
Creates a package.json file which stores the dependencies information for the app

## add Babel - Terminal


yarn add @babel/cli

yarn add @babel/preset-env

yarn add @babel/core

yarn add @babel/plugin-proposal-object-rest-spread


#### yarnlock
Stores cash data

#### node_modules
Project dependencies

#### babel
Transforms the files in a way that all browsers can understand

* **.babelrc**
```

{
	"presets": ["@babel/preset-env"],
	"plugins": ["@babel/plugin-proposal-object-rest-spread"]
}

```

preset env understands the development environment in which we're working on and converts the features to other code

#### add script with watch parameter


"scripts": {
    "dev": "babel ./main.js -o ./bundle.js -w"
}

