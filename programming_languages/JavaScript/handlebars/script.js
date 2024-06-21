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
"{{#each names}} Hello {{ name}} \n{{/each}}"; +
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
console.log(message);
// Hello, Germain
// Hello, John Doe
// Hello, Petrus
// Hello, Max Müller



messageNumber = "\n3---------------";
template = "" +
"I can call a function:\n" +
"{{myCustomFunction 'Parameter1' 'Parameter2 - vocals uuuuu' }}";
context = { 

};

Handlebars.registerHelper('myCustomFunction', function(param1, param2) {
    param1 = Handlebars.escapeExpression(param1);
    param2 = Handlebars.escapeExpression(param2);

    return `Reversed Param1: ${param1.split("").reverse().join("")}, Param2: ${param2.split("").filter( ( char) => ['a', 'e', 'i', 'o', 'u'].includes(char)).join("")}`;
    });

insertIntoTemplate = Handlebars.compile(template);
message = insertIntoTemplate(context);

console.log(messageNumber)
console.log(message);
// Reversed Param1: 1retemaraP, Param2: aaeeoauuuuu


messageNumber = "\n4---------------";
template = "" +
"I can access context objects:\n" +
"Person's name: {{ person.name }}";
context = {
    person: {
        name: "Germain"
    }
};

insertIntoTemplate = Handlebars.compile(template);
message = insertIntoTemplate(context);

console.log(messageNumber)
console.log(message);
// I can access context objects:
// Person's name: Germain



messageNumber = "\n5---------------";
console.log(messageNumber)
template = "" +
"I can access context objects and evaluate their context directly:\n" +
"This is the person: {{#with person }}{{ name }}{{/with }}";

context = {
    person: {
        name: "Germain"
    }
};

insertIntoTemplate = Handlebars.compile(template);
message = insertIntoTemplate(context);

console.log(message);
//I can access context objects and evaluate their context directly:
//This is the person: Germain

messageNumber = "\n6---------------";
console.log(messageNumber)
template = "" +
"I can make 'for loops' with context access:\n" +
"Persons:\n" +
"{{#each persons}} " +
"Hello {{ name }}! I heard you have {{ age }} yo\n" +
"{{/each}}";
//"This is the person: {{#with person }}{{ name }}{{/with }}";

context = {
    persons: [{
        name: "Germain",
        age: 17,
    }, {
        name: "John Doe",
        age: 15,
    }, {
        name: "Petrus",
        age: 20,
    }, {
        name: "Max Müller",
        age: 18,
    }]
};

insertIntoTemplate = Handlebars.compile(template);
message = insertIntoTemplate(context);

console.log(message);
//I can access context objects and evaluate their context directly:
//This is the person: Germain



messageNumber = "\n7---------------";
console.log(messageNumber)
template = "" +
"I can also change back to the parent context by using '..':\n" +
"{{#each persons}}" +
"Hello {{ name }}! I heard you have {{ age }} yo\n" +
"And look here what I found:  {{../parentContextItem}}\n" +
"{{/each}}";

context = {
    persons: [{
        name: "Germain",
        age: 17,
    }],
    parentContextItem: "This is the parent context"
};

insertIntoTemplate = Handlebars.compile(template);
message = insertIntoTemplate(context);

console.log(message);
// I can also change back to the parent context by using '..':
// Hello Germain! I heard you have 17 yo
// And look here what I found:  This is the parent context