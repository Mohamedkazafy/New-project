let password = document.getElementById("password")
let email = document.getElementById("email")
let btn = document.getElementById("btn")

btn.addEventListener("click",function(e){
    if(password.value === ""||email.value === ""){
        alert("please fill these filled")
        e.preventDefault()
    }
    else{
        window.location.href = 'select.html'
    }
})