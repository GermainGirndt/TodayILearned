# TSConfig - Paths
* **Plugin for using @path shortcuts**

```
yarn add tsconfig-paths -D
```

* **register in scripts**

```
-r tsconfig-paths/register
```

eg.
```
    "scripts": {
        "build": "tsc",
        "dev:server": "ts-node-dev -r tsconfig-paths/register --inspect --transpileOnly --ignore-watch node_modules src/shared/infra/http/server.ts",
        "start": "ts-node src/shared/infra/http/server.ts",
        "typeorm": "ts-node-dev -r tsconfig-paths/register ./node_modules/typeorm/cli.js"
    },

```