# JavaScript - Local Storage

## Saving and retrieving items from Local Storage



* **saving** -> executed when item is modified (list_todos)
```
function saveToStorage() {
    //globally avaiable
    // local storage doesn't save arrays -> converts to Djason
    // save the variable todos under the entry list_todos
    localStorage.setItem('list_todos', JSON.stringify(todos));
}
```

* **loading** -> on page start
```

// parse string
// if error -> [] (||)
var todos = JSON.parse(localStorage.getItem('list_todos')) || [];

```