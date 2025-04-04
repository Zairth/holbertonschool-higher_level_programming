let element = document.getElementById("list_movies");

async function fetches() {
    let response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
    let data = await response.json();
    for (index of data.results) {
        element.innerHTML += `<li>${index.title}</li>`;
    }
}

fetches();