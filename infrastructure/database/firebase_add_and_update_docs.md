## Firebase - Adding and Updating Values

##### Connect your JS with the DB
```
// Your web app's Firebase configuration

var firebaseConfig = {
apiKey: "AIzaSyDP5PWYVd0dKKJbutfNYuoJivl6BMLTwug",
authDomain: "colegio-87b4a.firebaseapp.com",
databaseURL: "https://colegio-87b4a.firebaseio.com",
projectId: "colegio-87b4a",
storageBucket: "colegio-87b4a.appspot.com",
messagingSenderId: "2618193921",
appId: "1:2618193921:web:b637412a64067125cea800",
measurementId: "G-QB0F2RZH15"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

const TURMA = "turmaA";
let db = firebase.firestore();
```

#### Adding new DOC to the database

```
// Adding to the database
// db.collection(TURMA).add({
//     nome: "Marcos",
//     sobrenome: "Santos",
//     notas: {nota1: 9.6, nota2:7.5},
// }).then((doc) => {
//     console.log("Documento inserido com sucesso:", doc);
// }).catch(err=>{
//     console.log(err);
// })

```


#### Setting values without merge - no data integrity
```
// Adding a document by name to the database (or updating, since it's a set method)
// And be careful: it overwrites the whole document, including the the parameters that aren't especifically being modified.
// db.collection(TURMA).doc("AlunoNovo").set({
//     nome: "Mariana2",
//     sobrenome: "Santos",
//     notas: { nota1: 8.6, nota2: 7.5},
// }).then((doc) => {
//     console.log("Documento inserido com sucesso:", doc);
// }).catch(err => {
//     console.log(err);
// })
```

#### Setting values with merge - provides data integrity
```
// if merge is set to true, then it just merges and maintains the preexisting data
db.collection(TURMA).doc("AlunoNovo").set({
   nome: "Mariana",
    sobrenome: "Santos",
}, {merge: true}).then((doc) => {
    console.log("Documento inserido com sucesso:", doc);
}).catch(err => {
    console.log(err);
})
```


#### Updating existing values - Data Integrity

```
db.collection(TURMA).doc("AlunoNovo").update({
   nome: "Ângelo",
    sobrenome: "Santos",
}).then((doc) => {
    console.log("Documento inserido com sucesso:", doc);
}).catch(err => {
    console.log(err);
})
```
