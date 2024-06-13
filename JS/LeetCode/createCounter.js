function creatCounter(n) {
    let counter = n
    return function() {
        return counter++
    }
}

const counter = creatCounter(10);

console.log(counter());
console.log(counter());
console.log(counter());

