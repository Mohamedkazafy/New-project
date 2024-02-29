let form = document.getElementById("form")
let firstName = document.getElementById("firstName")
let job = document.getElementById("job")
let cash = document.getElementById("phoneNumber")
let profileImage = document.getElementById("userImage")
let national = document.getElementById("id")
let btn = document.getElementById("btn")
let about = document.getElementById("about")
let years = document.getElementById("Exp")
form.addEventListener("submit",function(e){
    e.preventDefault()
    const firstNameValue = firstName.value
    const jobValue = job.value
    const AboutValue = about.value
    const cashValue = cash.value
    const nationalValue = national.value
    const expYears = years.value
    localStorage.setItem('firstName', firstNameValue)
    localStorage.setItem('job', jobValue)
    localStorage.setItem('Cash', cashValue)
    localStorage.setItem('national',nationalValue)
    localStorage.setItem('Exp',expYears)
    localStorage.setItem('about',AboutValue)
    window.location.href = "profile.html"
})
