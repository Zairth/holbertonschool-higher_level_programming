let element = document.querySelector("header");
let elementToClick = document.getElementById("red_header");

elementToClick.addEventListener("click", function (e) {
    let currentColor = getComputedStyle(element).color;
    if (element.style.color === "rgb(255, 0, 0)") {
        element.style.color = "black";
    } else {
        element.style.color = "#FF0000";
    }
});
