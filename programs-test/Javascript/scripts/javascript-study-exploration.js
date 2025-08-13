// javascriṕt resume

var testVar = "Hello friend, this a var"; // global scope and can be redeclared
let testLet = "Hello friend, this is a let"; // block scope and cannot be redeclared, just reassigned. But in this case, it is global.
const testConst = "Hello friend, this is a const"; // block scope and cannot be redeclared. But in this case, it is global.

function typerEffect(text, output) {
  const typer_outputs = document.getElementsByClassName("write_effect"); /* the function will be executed in
all elements that own class write_effect */
  const common_output = document.getElementById("standard_output"); // common output for the functions
  let index = 0;
  const delay = 50; // milliseconds
  const cursor = document.createElement("span");
  cursor.className = "cursor_blink"; 
  cursor.textContent = "|";
  function typer() {
    if (index < text.length) {
      output.textContent += text[index];  // Change the textual content of the element 
      index++;
      setTimeout(typer, delay);
    }
    else {
      output.appendChild(cursor);
            
    }
  }
  typer();
} /* could also use a function self-invoking

for (let elem of typer_outputs) {
  typerEffect(testLet, elem);
} */

function comparasionOperators() {
  let a = 1; let b = "1";
  let c = 1; let d = 1;

  // "equal to" operator, make a value comparison between two objects
  if (a == b) {
    console.log(`a: ${a} is equal to b: ${b} in value "=="`);
  } else if (a === b) // make a value and type comparison between two objects
    console.log(`a: ${a} is equal to b: ${b} in type and value "==="`);
  else {
    console.log(`a: ${a} is different from b: ${b} in value "==" and type and value "==="`);
  } // !== and !=== follow the same logic

  ternaryComparasion1 = c === d ? console.log(`c: ${c} is equal to d: ${d} in type and value "==="`) : console.log(`c: ${c} is different from d: ${d} in type and value "==="`);
  ternaryComparasion2 = c == d ? console.log(`c: ${c} is equal to d: ${d} in value "=="`) : console.log(`c: ${c} is different from d: ${d} in value "=="`);
}

function dataTypes() {
  // Booleans
  boolean0 = true;
  boolean1 = false;

  // Integers
  integer = 0;

  // Strings
  string = "Hi";

  // A simple object. Because all javascript object already work internally and are in dictonary format
  const person = {"name": "Guts", "age": 17};
  // Create an object:
  // const person = {};
  // Add properties:
  // person.name = "gus";
  // person.age = 17;

  // Array object
  const numbers = [1, 2, 3, 4, 5];

  // Date object. The "new" is used to declare an object returned by the function
  const date = new Date("2025-08-13");

  // undefined
  let undefinedValue;
}

// Arrow function
// Classes
// Js Browser DOM
// JS Web APIs
// Js AJAX
// JS Sets & Maps
// JS Async
