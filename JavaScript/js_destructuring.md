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