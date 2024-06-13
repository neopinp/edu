/* let randomNum = (Math.random());

let randomNum6 = Math.floor(Math.random() * 6); // random number between 0 and 6 

let randomMin6= Math.floor(Math.random() * 100 + 1); // between 1-100 + 1 sets minimum 
console.log(randomNum);
console.log(randomNum6);
console.log(randomMin6);



const max = 100;
const min = 50;

let randomNumMax = Math.floor(Math.random() * (max-min) + min); // generates a random number 50 - 100 
console.log(randomNumMax);
*/

const myButton = document.getElementById("myButton");
const myLabel1 = document.getElementById("myLabel1");
const myLabel2 = document.getElementById("myLabel2");
const myLabel3 = document.getElementById("myLabel3");
const min = 1;
const max = 6;
let randomNum1;
let randomNum2;
let randomNum3;


myButton.onclick = function(){
    randomNum1 = Math.floor(Math.random() * (max)) + min;
    randomNum2 = Math.floor(Math.random() * (max)) + min;
    randomNum3 = Math.floor(Math.random() * (max)) + min;
    myLabel1.textContent = randomNum1;
    myLabel2.textContent = randomNum2;
    myLabel3.textContent = randomNum3;
}
