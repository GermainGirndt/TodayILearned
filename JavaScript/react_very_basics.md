# React


## Getting started
```
npx create-react-app my-app --template=typescript
cd my-app
npm start
npm install react-icons
npm install react-router-dom
npm install @types/react-router-dom -D


# for maps
npm install @types/react-leaflet -D
```


## Notes
```
request -> comes with metadata (eg. user data, e-mail, password, and other embbed parameters)  
response -> response in browser  

RESTful -> Category for determined APIs. If an API matches it's creteria, then it's a RESTful API.  
SPA - Simple Page Application -> when thange between pages doesn't require the complete wellpage load  

REACT -> Framework
Main REACT Package + Other packages with REACT (REACT JS  + REACT Native)
REACT's benefits -> a single API, multiple clients (Mobile, Computer)
```

## Hello World, Modules and States

* **App.tsx**
```
// { useState} for using not only the first state of a variable/const, but also the new state
import React, { useState } from 'react';
import './App.css';

// JSX: The X addition allow to write xml syntax (html) inside js

import Header from './Header';

function App() {
  // defining states inside a function
  // uses useState for using not only a the initial vale but also the new value
  const [counter, setCounter] = useState(0); // [state value, function for atualizing the value state]

  function handleButtonClick() {
    // setting new counter value
    setCounter(counter +1);

  }
  return (
    <div>
      {/*  passing in 'Hello World' as title to the Header'*/} 
      <Header title = "Hello World"/>
      <Header title = "Hello World 2"/>
      <h1>Conteúdo da Aplicação</h1>
      {/*  using the const defined in the function */} 
      <h2>{counter}</h2>
      <button type="button" onClick={handleButtonClick}>Aumentar</button>

    </div>
  );
}

export default App;

```

* **Header.tsx**

```
import React from 'react';

// TypeScript -> Set title as required
interface HeaderProps {
    title: string;
}


// Every component starts with a capital letter, so that it doesn't matches the tags
// function header -> const Header = () [a function inside a constant]
// header: React.FC -> A type of function for using more parameters 
const Header: React.FC<HeaderProps> = (props) => {
    return (
        <header>
            {/* Using the javascript element passed in as title by the index.tsx file*/}
            <h1>{props.title}</h1>
        </header>
    );
}

export default Header;
```