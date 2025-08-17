// javascriṕt resume

var myVar = "this a var"; // global scope and can be redeclared
let myLet = "this is a let"; // block scope and cannot be redeclared, just reassigned. But in this case, it is global.
const myConst = "this is a const"; // block scope and cannot be redeclared. But in this case, it is global.

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
}

function outputs() {
  // other ways to obtain elements
  let writeEffect_output = document.querySelectorAll("p.write_effect");
  stdoutbyname = document.querySelector("#container0 span[name='stdout']");
  stdout_DOM.innerHTML = "with innerHTML (:"; // Insert text ou code directly in HTML *danger*
  stdout_DOM.textContent = "with textContent (:"; // Insert just text in element
  stdoutbyname.textContent = "with querySelectorAll";
//  document.write("Using document.write()"); // Insert text ou code directly in HTML *danger, especially if the document has not yet been fully loaded*
}

function dataTypes() {
  /* Almost all data in JS is an object. These are primitive data types, but they can be transformed into temporary objects when one
  of their methods is called.
  */
  console.log("Javascript datatypes:")

  // Booleans
  boolean0 = true;
  boolean1 = false;

  // Integers
  integer = 0;

  // Strings
  string = "Hi, my name is Gustavo (;";

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

  // Strings methods
  let slicedString = string.slice(15, 22);
  console.log(`Before: ${string}\nAfter "slice" method: ${slicedString}\n`);

  let stringUpperCase = string.toUpperCase();
  let stringLowerCase = string.toUpperCase();
  console.log(`String upper and lower case:\nUpper: ${stringUpperCase}\nLower case: ${stringLowerCase}\n`);

  let stringReplace = string.replace("Gustavo", "Elliot");
  console.log(`String replace method: ${stringReplace}\n`)

  // Numbers methods
  let bigInt = BigInt(100);
  console.log(`BigInt number: ${bigInt}`)

  let NumberTostr = toString(numbers[0]);
  console.log(`Number to string: ${NumberTostr}`);
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

function arrays() {
  // main Array methods
  let simpleArray = [1, 2, 3, 4, 5];
  let ArrayObject = new Array (1, 2, 3, 4, 5);
  console.log(`simple Array: ${simpleArray}\nArray object: ${ArrayObject}`, ArrayObject);

  console.log("Using simple array for examples!");
  console.log("Return array length:", simpleArray.length); // array length
  console.log("at() method to return first element:", simpleArray.at(0), "\nat() method to return last value:", simpleArray.at(-1)); // Return element by index
  console.log(`Replace an element value of a array. Before: ${simpleArray}`);
  simpleArray[0] = 2; // replace an element of an Array
  console.log(`After replace: ${simpleArray}`);
  console.log("Remove the first element from array (shift()). Before:", simpleArray);
  simpleArray.shift();
  console.log("After (shift()):", simpleArray);
  console.log("Remove the last element from array (pop()). Before:", simpleArray)
  simpleArray.pop();
  console.log("After (pop()):", simpleArray);
  console.log("Add new value at the end of the array (push()). Before:", simpleArray)
  simpleArray.push(6);
  console.log("After (push()):", simpleArray);
  console.log("Return index according to element (indexOf()):", simpleArray.indexOf(3));
  console.log("Removes or adds an element to the array (splice(index, count to del, value)). Before:", simpleArray);
  simpleArray.splice(0, 0, 1);
  console.log("After:", simpleArray);
  console.log("Reverse a array (reverse()). Before:", simpleArray);
  simpleArray.reverse();
  console.log("After:", simpleArray);
  console.log("Iterate over array elements, executing a function for each of them (forEach(function, element)). :");
  console.log("Print element for each element from array:");
  function printElement(e) {console.log(e)};
  simpleArray.forEach(printElement);
  console.log("Iterate over each element of the array, and modify the array (map(function refer)). Before:", simpleArray);
  function toStringNums(num) {return num.toString()};
  let toString = simpleArray.map(toStringNums);
  console.log("After:", toString);
  
}

// Javascript objects
function objectsJs() {
  console.log("Javascript objects:")

  const Person0 = {
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
  const PersonObj = Object.create(Person0);
  PersonObj.age = 18;
  console.log("Object person0: ", Person0, "\nObject create and update: ", PersonObj);
  
  //console.log(person1);

  // Js object from entries
  const linux_subsystems = [["nl80211", "subsystem"],["cfg80211", "subsystem"],["mac80211", "framework to SoftMAC wifi drivers"]];
  const myObj = Object.fromEntries(linux_subsystems);
  console.log(myObj.mac80211);

  const Person1 = {firstname: "Anna", lastname: "Moraes", age: 16};
  
  // Assign source properties to target
  console.log("Object assing: ", Object.assign(Person0, Person1));

  /* Constructors functions are used with "new" to create or initialize objects, or return an object directly.
  "this" is similar to python "self" in that both are used to refer to the instance itself, but the value of "this" depends on how
  the function is called.
  */
  function Person2(name, age, sex) {
    this.name = name;
    this.age = age;
    this.sex = sex;
  }

  let Person2Obj = new Person2("gustavo", 17, "masculine");
  console.log(Person2Obj);
  // Add a new Property
  Person2.prototype.country = "Brazil";
  Person2Obj = new Person2("gustavo", 17, "masculine");
  // console.log(`Defining a new value (prototype) in ${Person2Obj}: `); Wrong!!!
  console.log("Defining a new value (prototype) in", Person2Obj, " ");

  // Objects destructuring
  let {name, age} = Person2Obj;
  let numbers = [1, 2, 3, 4, 5];
  let [one, two] = numbers;
 
  console.log("Destructuring Object 'Person2': ", {name, age});
  console.log(`Destructuring Array "numbers": ${[one, two]}`);
}

// JS JSON (JavaScript Object Notation)
function json() {
  let JSobject = {
    Name: "Gustavo",
    Age: 17,
    Country: "Brazil",
    Sex: "Masculine"
  }; // This is an just javasript object

  console.log("Javascript Object", JSobject);
  let jsonData = JSON.stringify(JSobject);
  console.log(`Javascript Object to JSON string, with stringify method: ${jsonData}`);
  let ObjToJSON = JSON.parse(jsonData);
  console.log("JSON string", jsonData, "to Javascript Object, with the method JSON.parse():", ObjtoJSON);
}

// JS Switch
function switchs(num) {
  switch (num) {
    case 0:
      console.log(true);
      break;
    case 1:
      console.log(false); 
      break;
    default:
      console.log(` ${num} isn't 0 or 1 );`);
  };
}

// Classes
function classes() {
  class PersonFullname {
    constructor(name) {
      this.fullname = name;
    }
    present() {
      return "Fullname is " + this.fullname;
    }
  }

  // Methods inheritance
  class PersonData extends PersonFullname {
    constructor(fullname, country) {
      super(fullname); // Run the parent class constructor and initalize the "this" of the child class
      this.country = country;
    }
    show() {
      return this.present() + " and the country is " + this.country;
    }
    static any() {
      return "\nanything"
    }
  }
  PersonDataObj = new PersonData("Gustavo Araújo", "Brazil");
  console.log(PersonDataObj.show(), PersonData.any());
}

// iterations
// Promisses
// Typed arrays
// RegExp
// Js Browser DOM
// JS Web APIs
// Js AJAX
// JS Sets & Maps
// JS Programming
