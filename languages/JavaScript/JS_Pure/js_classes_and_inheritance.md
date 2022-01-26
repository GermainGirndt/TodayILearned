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


#### Example 2

```

class Usuario {
    constructor(email, password) {
        this.email = email;
        this.password = password;
        this.admin = false

    }

    isAdmin() { return this.admin}
}


class Admin extends Usuario {
    constructor(email, password) {
        super(email, password);
        super.admin = true;
    }
}

const User1 = new Usuario('email@teste.com', 'senha123')
const Admin1 = new Admin('email@teste.com', 'senha123')

console.log(User1.isAdmin())
console.log(Admin1.isAdmin())
```