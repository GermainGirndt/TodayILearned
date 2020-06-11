# JS and DOM




## Example 1 - Query Selector


### Body - Base Code
```
<div id="app">
    <input type="text" name="nome" id="nome"/>
    <button class="botao">Adicionar</button>
</div>
```

#### Get Element

```
// just return te element (id is always unique)
var inputElement = document.getElementById('nome');

// Always returns a vector (may not be unique)
var inputElement = document.getElementsByTagName('input');

// always returns a vector (may not be unique)
var inputElement = document.getElementsByClassName('input');
```

#### Query Selector - Searching over the DOM tree
```
var inputElement = document.querySelector('div#app input');
var inputElement = document.querySelectorAll('input');
console.log(inputElement);


// alternativelly ... input[name=nome]
var inputElement = document.querySelector('input#nome')
var btnElement = document.querySelector('button.botao')

btnElement.onclick = function() {
    var text = inputElement.value;
    alert(text);
}
```

## Example 2 - Adding and Removing Childs


### Body - Base Code
```
<div id="app">
    <input type="text" id="nome">
</div>
```


### Script - Creating a link element
```
    // <a href="http://rocketseat.com.br">Acessar site da RocketSeat</a>
    
    // Creating a tag
    var linkElement = document.createElement('a');
    linkElement.setAttribute('href', 'http://rocketseat.com');

    // putting the text into it
    var textElement = document.createTextNode('Acessar site da RocketSeat');
    linkElement.appendChild(textElement);

    // putting it in the div#app
    var containerElement = document.querySelector('#app');
    containerElement.appendChild(linkElement);

    // removing the input#nome tag
    var inputElement = document.querySelector('#nome');
    containerElement.removeChild(inputElement);

```

## Example 3 - Edit CSS

```
    <div id="app">
        <div class="box">
        </div>
    </div>
    <script>
        var boxElement = document.querySelector('.box');

        boxElement.style.width = "100px";
        boxElement.style.height = "100px";
        boxElement.style.backgroundColor = '#f00000';
        console.log(boxElement)
    </script>

    ```



## Example 4 - Adding a red square by button click

```
    <button type="text" onclick="createSquare()">Create Square</button>

    <script>
        console.log("Script")
        function createSquare(){
            console.log("Click")
            var newDiv = document.createElement('div');
            newDiv.style.width = "100px";
            newDiv.style.height = "100px";
            newDiv.style.backgroundColor = "#ff0000";
            console.log(newDiv)
            var containerElement = document.querySelector('body');
            containerElement.appendChild(newDiv);
        }
    </script>
```


## Example 5 - Generating squares and changing it's color randomly on click

```
    <button type="text" onclick="createSquare()">Create Square</button>

    <script>
        console.log("Script")

        function getRandomColor() {
        console.log('New color generated')
        var letters = "0123456789ABCDEF";
        var color = "#";
        for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
        }

        function setRandomColor(element){
            console.log("element:" + element)
            var newColor = getRandomColor(); 
            console.log("new color" + newColor)

            element.style.backgroundColor = newColor;

        }

        function createSquare(){
            console.log("Click")
            var newDiv = document.createElement('div');
            newDiv.style.width = "100px";
            newDiv.style.height = "100px";
            newDiv.style.backgroundColor = "#ff0000";
            newDiv.setAttribute('onclick','setRandomColor(this)')
            console.log(newDiv)
            var containerElement = document.querySelector('body');
            containerElement.appendChild(newDiv);
        }
    </script>

```


## Example 5 - Creating a ul in a blank html

```
// obs: mit [ x of ix ] = x -> index
    var nomes = ["Diego", "Gabriel", "Lucas"];

    var body = document.querySelector('body');

    var ul = document.createElement('ul'); 
    body.appendChild(ul);


    for (let nome of nomes){
        var nomeTextNode = document.createTextNode(nome);
        var li = document.createElement('li');
        li.appendChild(nomeTextNode);
        ul.appendChild(li);

    }

    </s
```

## Example 6 - Before x After

* **Before**
```
newDiv.setAttribute('onclick','setRandomColor(this)')
```
* **After**
```

newDiv.onClick('setRandomColor(this)')


```