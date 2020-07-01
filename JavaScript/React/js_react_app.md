# React App

# Styled-components

```
yarn add styled-components
yarn add polished
yarn add react-icons

```

### Uses/Benefits
* for scopping the css with react
* every css file is for standard global
* note: install the VSCode Plugin - styled components for syntax highlighting


### Implementing on Code

* **styles.css -> styles.js/ts**
```
import styled from "styled-components";

export const Title = styled.h1`
  font-size: 48px;
  color: #3a3a3a;
`;

```


* **index.ts/js - import css**

```
import React from "react";
import { Title } from "./styles";

const Dashboard: React.FC = () => {
  return <Title>Explore GitHub Repositories</Title>;
};

export default Dashboard;

```


### Adding Global Style with Styled-Components


* **Create global style file** SRC-ROOT: styles/global.ts

```
import { createGlobalStyle } from "styled-components";

export default createGlobalStyle`
    * {
        margin: 0;
        padding: 0;
        outline: 0;
        box-sizing: border-box;
    }

    body {
        background: #F0F0F5;
    }
`;


```

* **Add it to the App's main file (normally App.tsx)**

```
import React from "react";
import { BrowserRouter } from "react-router-dom";

import GlobalStyle from "./styles/global";
import Routes from "./routes";

const App: React.FC = () => (
  <>
    <BrowserRouter>
      <Routes />
    </BrowserRouter>
    <GlobalStyle />
  </>
);

export default App;


```