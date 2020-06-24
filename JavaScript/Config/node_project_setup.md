# Node Project Setup

# Code


```
yarn init -y
yarn add express
yarn add typescript -D
yarn tsc --init
yarn add @types/express
yarn add eslint@6.8.0 -D
yarn eslint --init
yarn add @typescript-eslint/eslint-plugin@latest eslint-config-airbnb-base@latest eslint-plugin-import@^2.21.2 @typescript-eslint/parser@latest -D
yarn add prettier eslint-config-prettier eslint-plugin-prettier -D
```

* **For more notes to ESLint, check** https://www.notion.so/ESLint-7e455a7ac78b424892329ee064feaf99#ebfba68e55584ef1a97d860c3f0b9eef



Set "rootDir" to 
```
"rootDir": "./src"
```

## Before running the code

```
yarn tsc
```


## Live reload + Typescript

```
yarn add ts-node-dev -D
```


## Add scripts

  "scripts": {
    "build": "tsc",
    "dev:server": "ts-node-dev --transpileOnly --ignore-watch node_modules src/server.ts"
  },

  --transpileOnly for not showing errors (let just the VSCode do this)
  --ignore-watch node_modules for not watching node modules changes

