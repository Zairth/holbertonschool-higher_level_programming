let element = document.querySelector(".my_list");
let elementToClick = document.getElementById("add_item");

elementToClick.addEventListener("click", function (e) {
    let li = `<li>Item</li>`;
    element.innerHTML += li;
});
