## Javascript - Array Operations

#### Base
``` 
const arr = [1, 3, 4, 5, 8, 9];
```
#### Map
const newArr = arr.map(function(item, index){
    return item + index

})

console.log(newArr);

#### Reduce
```
const minus = arr.reduce(function(total, nextValue){
    return total - nextValue
})


console.log(minus)
```

#### Filter
```
const filter = arr.filter(function(item) {
    return item % 2 === 0;
});

console.log(filter)
```
#### Find
* Either returns the first item which the expression is true or returns nothing
```
find = arr.find(function(item) {
    return item === 2;
})

console.log(find);
```