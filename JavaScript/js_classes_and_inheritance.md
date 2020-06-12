## JavaScript Class and Inheritance

#### Example

````

class List {
    constructor() {
        this.data = [];
    }

    add(data){
        this.data.push(data);
        console.log(this.data);
    }
}


class TodoList extends List {
    constructor() {
        super();

        this.usuario = 'Diego';
    }
    mostraUsuario() {
        console.log(this.usuario);
    }
}

    const MinhaLista = new TodoList();

    document.getElementById('novotodo').onclick = function() {
        MinhaLista.add('Novo todo');
    }

```