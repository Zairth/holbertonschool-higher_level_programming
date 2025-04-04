document.addEventListener('DOMContentLoaded', async function () {
        let element = document.getElementById("hello");
        let response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
        let data = await response.json();
        element.innerHTML += `${data.hello}`;
});
