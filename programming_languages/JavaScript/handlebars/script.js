const Handlebars = require('handlebars');

let messageNumber = "\n1---------------";
let template = "Hello, {{name}}";
let context = { name: "Germain" };

let insertIntoTemplate = Handlebars.compile(template);
let message = insertIntoTemplate(context);

console.log(messageNumber)
console.log(message); // Hello, Germain

messageNumber = "\n2---------------";
template = "" +
"{{#each names}}" +
"Hello, {{name}}\n" +
"{{/each}}" +
"";
context = { names: [
    {name: "Germain"},
    {name: "John Doe"},
    {name: "Petrus"},
    {name: "Max Müller"},
] };

insertIntoTemplate = Handlebars.compile(template);
message = insertIntoTemplate(context);

console.log(messageNumber)
console.log(message); // Hello, Germain



