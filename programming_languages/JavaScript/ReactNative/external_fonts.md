# React Native - External Fonts

### Project Root

* **Create react-native-config.js file**

* **Declare the font as assets**

```
module.exports = {
  project: {
    ios: {},
    android: {},
  },
  assets: ['./assets/fonts'],
};

```

### Terminal
```
$ yarn react-native link
```