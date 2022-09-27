## Gatsby Tutorial

### Install

```
sudo npm install -g gatsby-cli
```

### Using a starter

```
gatsby new hello-world https://github.com/gatsbyjs/gatsby-starter-hello-world
cd hello-world
gatsby develop
```

### Developing basic features

- **src/components/header.js**

```
import React from "react"

export default function Header(props) {
  return <h1>{props.headerText}</h1>
}
```

- **src/pages/index.js**

```
import React from "react"
import { Link } from "gatsby"
import Header from "../components/header"

export default function Home() {
  return (
    <div style={{ color: `purple` }}>
      <Link to="/contact/">Contact</Link>
      <Header headerText="Hello Gatsby!" />
      <p>What a world.</p>
      <img src="https://source.unsplash.com/random/400x200" alt="" />
    </div>
  )
}
```

- **src/pages/about.js**

* Right acessible through http://localhost:8000/about !

```
import React from "react"
import Header from "../components/header"

export default function About() {
  return (
    <div style={{ color: `teal` }}>
      <Header headerText="About Gatsby" />
      <Header headerText="It's pretty cool" />
      <p>Such wow. Very React.</p>
    </div>
  )
}
```

- **src/pages/contact.js**

```
import React from "react"
import { Link } from "gatsby"
import Header from "../components/header"

export default function Contact() {
  return (
    <div style={{ color: `teal` }}>
      <Link to="/">Home</Link>
      <Header headerText="Contact" />
      <p>Send us a message!</p>
    </div>
  )
}
```

### Deploying a Gatsby Website

- **Surge**
  Surge is one of many “static site hosts” which makes it possible to deploy Gatsby sites.

- **Install and create account**

```
npm install --global surge

```

```
surge login

```

or

```
npx surge login
```

- **Build the website**

```
yarn build
```

- **Deploy using surge**

```
surge public/
```
