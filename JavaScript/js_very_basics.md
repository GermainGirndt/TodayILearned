## JS - Very Basics


### DOM - Document Object Model
DOM are basically all elements from the html. 

### Set interval and set time out

function exibeAlgo() {
    console.log('Hello World')
}

// Repeats over time
setInterval(exibeAlgo, 10000);

// Just executes once
setTimeout(exibeAlgo, 10000);


### Syntaxe Hints


* **Remember the ; between arguments**

```
        function pares(x, y) {
            if (x % 2 == 0) 
                for ( let start = x; x <= 321; x += 2)
                    console.log(x);
            else
                for (let start = x+ 1; x <= 321; x += 2)
                    console.log(x)
        }
        pares(32, 321);
```

* **for LET ... of ...** -> like python
```
            for (let skill of skills) {
                if (skill == "Javascript") console.log(true)
                else console.log(false)
            }
        }
        var skills = ["Javascript", "ReactJS", "React Native"];
        temHabilidade(skills); // true ou false

```

* **for LET ... in ...** -> IN -> INDEXES
```

very_confuse = [99, 154, 444]

for (let x in very_confuse) console.log(x)

// prints 
/  0
// 1
// 2


```
* **join with javascript is exactly the contrary of python**

```

    function printHabilidades(usuarios){
        for (usuario of usuarios){
            console.log(`O ${usuario.nome} possui as habilidades: ${usuario.habilidades.join(', ')}`); 

            // on python it would be ', '.join(usuario.habilidades))_


        }
    }

    printHabilidades(usuarios)


```