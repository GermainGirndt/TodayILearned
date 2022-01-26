

### Terminal

yarn add react-native-vector icons


### Add to android/app/build.gradle

```
project.ext.vectoricons = [
  iconFontNames: ['Feather.ttf']
];

apply from: "../../node_modules/react-native-vector-icons/fonts.gradle"
```