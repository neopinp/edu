/* constants 

const = a variable that can't be changed once it has already been assigned*/

/*
const PI = 3.14159;// PI for numbers, pi for strings 
let radius;
let circumference;

let pi = 420;  // doesnt work because of const PI
 
radius = window.prompt("Enter the radius of a circle"); // get input from a window prompt (NOT PROFESSIONAL WAY)
radius = Number(radius);   // change type to number to process input 

circumference = 2 * pi * radius;
*/

//MORE PROFESSIONAL WAY BELOW VVVVVVV

document.getElementById("mySubmit").onclick = function(){
    radius = document.getElementById("myText").value;
    radius = Number(radius);
    circumference = 2 * PI * radius;
    document.getElementById("myH3").textContent = circumference + "cm";
}
