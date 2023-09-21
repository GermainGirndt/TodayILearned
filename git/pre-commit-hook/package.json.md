# Pre-Commit Hook

### Scripts

```
{"format": "prettier --write src/",
"prepare": "husky install && chmod 500 ./.husky/pre-commit"}
```

### Dependencies

```
"husky": "^8.0.3",
"lint-staged": "^14.0.1"
"eslint": "^8.42.0"
```

### Root

```
    "husky": {
         "hooks": {
             "pre-commit": "lint-staged"
         }
     },
     "lint-staged": {
         "*.{ts,vue}": [
             "npm run lint",
             "prettier --write"
         ]
     },
```
