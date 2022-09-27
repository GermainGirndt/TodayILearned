const empresa = {
    nome: 'Rocketseat',
    endereco: {
    cidade: 'Rio do Sul',
    estado: 'SC',
    }
   };


let {nome, endereco: {cidade, estado}} = empresa;
console.log(nome); // Rocketseat
console.log(cidade); // Rio do Sul
console.log(estado); // SC

/////////


const mostraInfo = ({nome, idade}) => `${nome} tem ${idade}` 

console.log(mostraInfo({ nome: 'Diego', idade: 23 }))


const arr = [1, 2, 3, 4, 5, 6];

const [x, ...y] = arr;

console.log(x); // 1
console.log(y); // [2, 3, 4, 5, 6]

// ///////////

const usuario = {
    nome: 'Diego',
    idade: 23,
    endereco: {
    cidade: 'Rio do Sul',
    uf: 'SC',
    pais: 'Brasil',
    }
   };


const usuario3 = {...usuario, endereco: {...usuario.endereco, cidade: 'Lontras'}}


console.log(usuario3)

const nome = 'Diego';
const idade = 23;
const usuario = {
 nome,
 idade,
 cidade: 'Rio do Sul',
};

console.log(usuario)