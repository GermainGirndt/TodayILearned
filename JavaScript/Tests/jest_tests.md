# Jest Tests

### Install
```
yarn add jest -D
```

### Use

```
yarn jest --init


```

### For use with typescript also

```
yarn add ts-jest -D
yarn add @types/jest -D
```

### For using @ paths shortcuts

* **jest.config.js**
```

const { pathsToModuleNameMapper } = require('ts-jest/utils');
const { compilerOptions } = require('./tsconfig.json');
...
    moduleNameMapper: pathsToModuleNameMapper(compilerOptions.paths, {
        prefix: '<rootDir>/src/',
    }),
```
* **jest.config.js**
```
preset: 'ts-jest'
```

### Config

* **jest.config.js**
```
    testMatch: [
      "**/*.spec.ts"
    ],
```

* **.eslintrc.json**
```
    "env": {
    	...,
        "jest": true
    },
```

### Run

```
yarn test
```