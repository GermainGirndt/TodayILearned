## Standard Commits

- **Note: order is important**

### Config and Install

- **Create a 'commitlint.config.js' file**

```
module.exports = {
  extends: ["@commitlint/config-conventional"],
};
```

- **Install libs**

```
yarn init -y
git init
yarn add @commitlint/config-conventional @commitlint/cli -D
yarn add husky -D
git add -A
```

- **Add husky config to package json**

```
"husky": {
    "hooks": {
        "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    }
}
```

### **Test**

- **Expected error**

```
git commit -m "Initial commit"
```

- **Expected success**

```
git commit -m "feat: add initial setup"
```

yarn add commitizen -D

yarn commitizen init cz-conventional-changelog --yarn --dev --exact
