// javascriṕt resume

var testVar = "Hello friend, this a var"; // global scope and can be redeclared
let testLet = "Hello friend, this is a let"; // block scope and cannot be redeclared 
const testConst = "Hello friend, this is a const"; // block scope and cannot be redeclared

const typer_outputs = document.getElementsByClassName("write_effect"); /* the function will be executed in
all elements that own class write_effect */
const common_output = document.getElementById("standard_output"); // common output for the functions

function typerEffect(text, output) {
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
} // could also use a function self-invoking

for (let elem of typer_outputs) {
  typerEffect(testLet, elem);
}
