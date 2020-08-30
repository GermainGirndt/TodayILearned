## Gatsby Tutorial - Part 2 - Styling

### Include the stylesheet in gatsby-browser.js

- **Create a CSS Stylesheet in ROOT/src/styles/global.css**

```
html {
  background-color: lavenderblush;
}
```

- **Create a 'src/gatsby-browser.js' file**
- gatsby-browser.js is one of a handful of special files that Gatsby looks for and uses (if they exist). Here, the naming of the file is important.

```
import "./src/styles/global.css"

// or:
// require('./src/styles/global.css')
```

### Working with CSS Modues

- **Create a container component in src/component/container.js**

```
import React from "react"
import containerStyles from "./container.module.css"

export default function Container({ children }) {
  return <div className={containerStyles.container}>{children}</div>
}

```

- **Create a CSS file (container.module.css) in the same directory (src/component/container.module.css)**

- Using module.css instead of the usual .css is how you tell Gatsby that this CSS file should be processed as a CSS module rather than plain CSS.

```
.container {
  margin: 3rem auto;
  max-width: 600px;
}
```

- **Create a new page component by creating a file at src/pages/about-css-modules.js**

```

import React from "react"
import styles from "./about-css-modules.module.css"
import Container from "../components/container"

console.log(styles)

const User = props => (
  <div className={styles.user}>
    <img src={props.avatar} className={styles.avatar} alt="" />
    <div className={styles.description}>
      <h2 className={styles.username}>{props.username}</h2>
      <p className={styles.excerpt}>{props.excerpt}</p>
    </div>
  </div>
)

export default function About() {
  return (
    <Container>
      <h1>About CSS Modules</h1>
      <p>CSS Modules are cool</p>
      <User
        username="Jane Doe"
        avatar="https://s3.amazonaws.com/uifaces/faces/twitter/adellecharles/128.jpg"
        excerpt="I'm Jane Doe. Lorem ipsum dolor sit amet, consectetur adipisicing elit."
      />
      <User
        username="Bob Smith"
        avatar="https://s3.amazonaws.com/uifaces/faces/twitter/vladarbatov/128.jpg"
        excerpt="I'm Bob Smith, a vertically aligned type of guy. Lorem ipsum dolor sit amet, consectetur adipisicing elit."
      />
    </Container>
  )
}

```

- **Create the file for the CSS at src/pages/about-css-modules.module.css**

```
.user {
  display: flex;
  align-items: center;
  margin: 0 auto 12px auto;
}

.user:last-child {
  margin-bottom: 0;
}

.avatar {
  flex: 0 0 96px;
  width: 96px;
  height: 96px;
  margin: 0;
}

.description {
  flex: 1;
  margin-left: 18px;
  padding: 12px;
}

.username {
  margin: 0 0 12px 0;
  padding: 0;
}

.excerpt {
  margin: 0;
}
```
