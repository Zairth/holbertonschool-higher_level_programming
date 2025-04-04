let element = document.querySelector("header");
let elementToClick = document.getElementById("toggle_header");

elementToClick.addEventListener("click", function (e) {
    if (element.classList.contains("green")) {
        element.classList.toggle("green");
        element.classList.toggle("red");
    } else {
        element.classList.toggle("red");
        element.classList.toggle("green");
    }
});
