# TypeScript
* Functions like Babel
* Converts the end code to javascript.
* With typescript, the Development Enviroment is more inteligent, recognizing the patterns.

## Install
```
yarn add typescript -D
yarn tsc --init
yarn add @types/express (or library)
yarn tsc
node src/index.js
---

``` 

## Other Config

* Configuration: change .js files output directory

```
outDir": "./dist
```



## Create React Project + Typescript


```
npx create-react-app my-app --template typescript
# or
yarn create react-app my-app --template typescript
```

## TypeScript Basic Settings
```
npm install --save typescript @types/node @types/react @types/react-dom @types/jest
# or
yarn add typescript @types/node @types/react @types/react-dom @types/jest
```


#### Example Project

* **routes.ts**
```
import { Request, Response } from "express";
import createUser from "./services/CreateUser";

export function helloWorld(request: Request, response: Response) {
  const user = createUser({
    name: "Germain M. Pereira",
    email: "pereira.germain@outlook.com",
    password: "123456",
    techs: [
      "Node.js",
      "ReactJS",
      "React Native",
      { title: "Javascript", experience: 100 },
    ],
  });

  return response.json({ message: "Hello World!" });
}
```

* **CreateUser.ts**
```
/**
 *
 * interface -> defines separately the data types
 */

interface TechObject {
  title: string;
  experience: number;
}

interface CreateUserData {
  name?: string; // name - optional
  email: string;
  password: string;
  techs: Array<String | TechObject>; // Array<format>
}

export default function createUser({ name, email, password }: CreateUserData) {
  const user = {
    name,
    email,
    password,
  };
  return user;
}

```