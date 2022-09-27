# JavaScript - Ajax

Asynchronous REquest - request from server without realoding the webpage

Promises just return a value after some time; 
until then, we're free to keep executing other code liens

## First request - GitHub API
```
var xhr = new XMLHttpRequest();

xhr.open('GET', 'https://api.github.com/users/GermainPereira');
xhr.send(null)

// listens the xhr states, while we can keep doing another activities
// if the response has came, execute function
xhr.onreadystatechange = funct ion () {
    if (xhr.readyState === 4) {
        console.log(JSON.parse(xhr.responseText));
    }
}
```


## Second Request - With Promises

```
var minhaPromise = function() {

    // Promise is a class
    // resolve and reject are also functions
    // by success -> resolve; by failure -> reject
    return new Promise(function(resolve, reject){
        var xhr = new XMLHttpRequest();
        xhr.open('GET','https://api.github.com/users/GermainPereira');
        xhr.send(null);

        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    resolve(JSON.parse(xhr.responseText));
                } else {
                    reject('Erro na requisição');
                }
            }
        }
    });
}

// resolve calls then;
// and passes in its argument as response
// reject call catch;
// and passes in its argument as catch
minhaPromise()
    .then(function(response) {
        console.log(response);
    })
    .catch(function(error){
        console.warn(error);
    });
```

# Third request - much more easier with axios

* **call axios' script**
```
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

```

* **call your script**

```
axios.get('https://api.github.com/users/GermainPereira')
    .then(function(response) {
        console.log(response);
    })
    .catch(function(error){
        console.warn(error);
    });
```


## Third Request - Function that returns a promise, that will be executed within 2 secs

```

function checaIdade(idade) {
    return new Promise (function (resolve, reject) {
        setTimeout(
            idade >= 18 ? () => resolve() : () => reject(), 2000
        );  
    });
}

checaIdade(20)
 .then(function() {
 console.log("Maior que 18");
 })
 .catch(function() {
 console.log("Menor que 18");
 });
```