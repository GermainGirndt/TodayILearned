# React Native Helper

* **For improving react native's cross-platform behaviour**

## Component/Page Styles

* **Import**
```
import { getBottomSpace } from 'react-native-iphone-x-helper';
```

* **Apply padding in order to avoid buttons in the bottom**
```
padding: 16px 0 ${16 + getBottomSpace()}px;
```
