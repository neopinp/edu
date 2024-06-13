// let username = window.prompt("What is your username?")


//professional way 
document.getElementById("mySubmit").onclick = function(){
    username = document.getElementById("myText").value;
// take new input username and set it to header text Content
document.getElementById("myH1").textContent = `Hello ${username}`;
}

