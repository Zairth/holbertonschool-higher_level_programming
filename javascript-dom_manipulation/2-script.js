let element = document.querySelector("header");
let elementToClick = document.getElementById("red_header");

elementToClick.addEventListener("click", function (e) {
    element.classList.toggle("red");
});
