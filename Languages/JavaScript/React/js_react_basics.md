# React

* **React** = Bib
* **ReactJS** = React + Facebook's React DOM
* **React Native** = React + Bib for Native Elements

## Notes


* **.jsx** = JS + xml (html syntax)
* **components:** visual (html) + function (js) + style (css)
	* **Every component** has a render method
	* **Every component** is for default a class 
 * **className** instead of class for not mixing with js



## Install

* **g** stands for global
```
npm install -g create-react-app
```

## Creating App
```
create-react-app PROJECTNAME
```

## Add React - Terminal
```
yarn init -y
yarn add react react-dom

```

## Install router
```
yarn add react-router-dom
```


* Rembember to Config Babbel and Webpack


## Code

#### Normal style

```
class Header extends Component {
    render() {
        return <h1>Hello world</h1>
    }
}
```


#### Stateless Components (function)

```
const Header = () => (
    <h1>Hello</h1>
);

```