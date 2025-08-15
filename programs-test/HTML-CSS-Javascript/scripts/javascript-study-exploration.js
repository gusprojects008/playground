// javascriṕt resume

var testVar = "Hello friend, this a var"; // global scope and can be redeclared
let testLet = "Hello friend, this is a let"; // block scope and cannot be redeclared, just reassigned. But in this case, it is global.
const testConst = "Hello friend, this is a const"; // block scope and cannot be redeclared. But in this case, it is global.

const stdout_DOM = document.getElementById("standard_output"); // standard output for the functions

function typerEffect(text, output) {
  const typer_outputs = document.getElementsByClassName("write_effect");
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

function outputs() {
  // other ways to obtain elements
  let writeEffect_output = document.querySelectorAll("p.write_effect");
  stdoutbyname = document.querySelector("#container0 span[name='stdout']");
  stdout_DOM.innerHTML = "with innerHTML (:"; // Insert text ou code directly in HTML *danger*
  stdout_DOM.textContent = "with textContent (:"; // Insert just text in element
  stdoutbyname.textContent = "with querySelectorAll";
//  document.write("Using document.write()"); // Insert text ou code directly in HTML *danger, especially if the document has not yet been fully loaded*
}


function comparasionOperators() {
  console.log("Javascript comparassion operators:")
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
  console.log("Javascript datatypes:")
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

/* javascript functions are not executed immediately. They are "saved for later use" and will be executed later, when
invoked (called upon). This is called "javascript hoisting" */
//functions();

function functions() {
  console.log("Javascript functions:")
  let a, b;
  a = 5;
  b = 10;

  // The function can be expressed in one variable
  const functest = function (a, b) {return `functest: ${a * b}`};
  console.log(functest(a, b));
   
  // Arrow function
  myArrowFunc = (a, b) => {return a * b};
  result = myArrowFunc(a, b);
  console.log("Arrow function: " + result);

  // self-invoking function
  // this is a self-invoked anonymous function
  (function (a, b) {console.log(`self-invoked anonymous function ${a * b}`);})(a, b);

  /* apply(): apply() is used to write a method that will be applied to differents objects, the arguments to the
  "fullName" function are passed in a list "[arg1, arg2]", useful for dynamic arguments
  */
  const person = {
    /*fullName: function (firstname, lastname) {
      return firstname + " " + lastname;
    }*/
    /*fullName: function () {
      return this.firstname + " " + this.lastname;
    }*/
    firstname: "guts",
    lastname: "araujo",
    fullName: function () {
      return this.firstname + " " + this.lastname;
    }
  };
  person1 = {
    firstname: "gustavo",
    lastname: "araújo"
  };
  console.log(person1);
  arg1 = person1.firstname;
  arg2 = person1.lastname;
  console.log(person.fullName.apply(Object, [arg1, arg2]));
  //console.log(person.fullName.apply(person1));

  /* call(): call() is used to call "fullName" by calling "person1", the arguments passed in "call()" to the function
  are separated by ",", unlike apply().
  */
  console.log(person.fullName.call(Object, arg1, arg2));

  /* with the bind() method, an object can borrow a method from another object */
  let fullName = person.fullName.bind(person1);
  console.log(fullName());
}

// Javascritp object
function objectsJs() {
  console.log("Javascript objects:")

  const person0 = {
    firstname: "gustavo",
    lastname: "araujo",
    age: 17,
    bool: true
  };
  /* better
  const person1 = new Object({
    firstname: "gustavo",
    lastname: "araujo",
    age: 17
  });
  */

  // crate a new person
  const personObj = Object.create(person0);
  personObj.age = 18;
  console.log("Object person0: ", person0, "\nObject create and update: ", personObj);
  
  //console.log(person1);

  // Js object from entries
  const linux_subsystems = [["nl80211", "subsystem"],["cfg80211", "subsystem"],["mac80211", "framework to SoftMAC wifi drivers"]];
  const myObj = Object.fromEntries(linux_subsystems);
  console.log(myObj.mac80211);

  const person1 = {firstname: "Anna", lastname: "Moraes", age: 16};
  
  // Assign source properties to target
  console.log("Object assing: ", Object.assign(person0, person1));
}

//outputs();



// Classes
// Js Browser DOM
// JS Web APIs
// Js AJAX
// JS Sets & Maps
// JS Async
