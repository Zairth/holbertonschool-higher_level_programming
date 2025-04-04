let element = document.querySelector("header");
let elementToClick = document.getElementById("update_header");

elementToClick.addEventListener("click", function (e) {
    let newHeader = "New Header!!!";
    element.innerHTML = newHeader;
});
