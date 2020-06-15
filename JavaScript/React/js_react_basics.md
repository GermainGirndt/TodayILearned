# React



## Notes

```
* **jsx** - not a simple html - but also js variables
* **Components:** visual (html) + function (js) + style (css)
	* **Every component** has a render method
	* **Every component** is for default a class 
 * **className** instead of class for not mixing with js
```

## Install

* g stands for global
```
npm install -g create-react-app
```

## Creating App
```
create-react-app PROJECTNAME
```

## Creating App
```
// stateless components (function)
const Header = () => (
    <h1>Hello</h1>
);

// normal would be

class Header extends Component {
    render() {
        return <h1>Hello world</h1>
    }
}
```