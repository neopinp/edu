"use strict";

function creatCounter(n) {
  var counter = n;
  return function () {
    return counter++;
  };
}

var counter = creatCounter(10);
console.log(counter());
console.log(counter());
console.log(counter());