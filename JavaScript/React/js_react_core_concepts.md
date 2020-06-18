
## Using Component and Passing in Props and Child
* **app.js**
```
function App() {
  const projects = ["Desenvolvimento de app", "Front-end web"];

  return (
    <>
      {/* pass in title as paramater */}
      <Header title="Homepage">
        <ul>
          <li>Homepage</li>
          <li>Projects</li>
        </ul>
      </Header>

      <Header title="Projects">
        <ul>
          <li>Homepage</li>
          <li>Projects</li>
          <li>Login</li>
        </ul>
      </Header>
    </>
  );
}

```


## Establishing the component, using the received props and child
```
import React from "react";

// Props = proprieties - param received from App automatically.
// Can be destructured to:
// title = param passed in
// children = content that the tag received (children from this tag by call)
export default function Header({ title, children }) {
  return (
    <header>
      <h1>{title}</h1>
      {children}
    </header>
  );
}

```

## Managing State

*  **'useState' function** returns an array with 2 positions:
*  1. the variable with it's initial state
*  2. a function for updating this value
```
function App() {
  const [projects, setProjects] = useState([
    "Desenvolvimento de app",
    "Front-end web",
  ]);
```

* **Imutability:** We're unable to alter variables
* for this purpouse, we need to change it completely
```
  function handleAddProject() {
    // Initially, 'projects.push(`Novo projeto ${Date.now()}`);''
    // the above methode, for instance, doesn't imutability.
    // Better:
    setProjects([...projects, `Novo projeto ${Date.now()}`]);
  }
```

* **Rest**

```
  return (
    <>
      <Header title="Projects" />

      <img width={200} src={backgroundImage} />

      {/* key is required by react. It's a unique element required for 1 level html */}
      <ul>
        {projects.map((project) => (
          <li key={project}>{project}</li>
        ))}
      </ul>

      <button type="button" onClick={handleAddProject}>
        Adicionar projeto
      </button>
    </>
  );
}

export default App;

```