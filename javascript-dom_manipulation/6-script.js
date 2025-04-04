let element = document.getElementById("character");

async function fetches() {
    let response = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
    let data = await response.json();
    element.innerHTML = `${data.name}`;
}

fetches();