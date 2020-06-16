## Javascript - Arrow Functions in 4 Steps

* Arrow functions are a perfect replacement for short anonymous functions

## Base Code
```
const arr = [1, 2, 3, 4, 5, 6];
```

#### 1.  write the original function
```
const newArr = arr.map(function(item) {

    return item * 2;

});
```

#### 2. remove the function keyword and add an arrow

```
const newArr = arr.map((item) => {

    return item * 2;

});
```

#### 3. if there's just one parameter, remove the parenthesis

```
const newArr = arr.map(item => {

    return item * 2;

});
```

#### 4. if there's just one line, move the returned value towards the arrow and erase the rest

```
const newArr = arr.map(item => item * 2);
```


----

#### Another possible examples

```
const test = () => {
    return 'teste';
}

const test = () => [ 1, 2, 3, 4]


const test = () => 'hey'


const test = () => ({nome: 'Germain'})
```

#### But not this (JS may confuse it with comparisons)
```
const test = () => {nome: 'Germain'}

```