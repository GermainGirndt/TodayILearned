## Javascript - Destructuring (with examples)


#### Base Code

```
const user = {
    name: 'Diego',
    age: 23,
    address: {
        city: 'Rio do Sul',
        state: 'SC',
    },
};
```


#### Before 1

```
const name = user.name;
const age = user.age;
const city = user.address.city;
const state = user.address.state;

console.log(name);
console.log(age);
console.log(city);
console.log(state);
```

#### After 1
* Unpacking attributes

```
const { name, age, address: {city, state} } = user;


console.log(name);
console.log(age);
console.log(city);
console.log(state);

```
---


#### Before 2

```
function showName(user) {
    console.log(user.name)
}

showName(user)
```

#### After 2
* JS destructures the arguments automatically

```
function showName({name}) {
    console.log(name)
}

showName(user)
```

#### Example 3

```
// REST

const user = {
    name: 'Diego',
    age: 23,
    group: 'Rocketseat'
};



const { name, ...rest} = user;

console.log(name);
console.log(rest);

```

#### Rest


```
function returnParams(...params){
    return params;
}

console.log(returnParams(1, 3, 4, 33));

// returns [1, 3, 4, 33]
```

#### SPREAD

* **unpacking elements**
```
const arr1= [1, 2, 3];
const arr2 = [4, 5, 6]

const arr3 = [ ...arr1, ...arr2];
// unpacks to [ 1, 2, 3, 4, 5, 6]
```

* **Creating a new oject with redefined attributes**

```
const usuario1 = {
    nome: 'Diego',
    idade: 23,
    empresa: 'Rocketseat'
}

// Redefines a new object
const usuario2 = {...usuario1, nome: 'Gabriel'};
```


#### Short Syntax


```
const nome = 'Diego';
const idade = 23;

const usuario = {
    // nome: nome
    nome,
    // idade: idade
    idade,
    empresa: 'Rocketseat'
};


console.log(usuario)
```