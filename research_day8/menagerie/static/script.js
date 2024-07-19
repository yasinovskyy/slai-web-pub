"use strict";

const BASE_URL = "http://localhost:5000/api/v1"

/**
 * Retrieve data using fetch
 * @param {*} url 
 * @returns JSON
 */
async function fetchData(url) {
    return fetch(url)
        .then(response => response.json())
        .catch(error => console.log(error));
}

async function getData(typeOfData) {
    let location = document.querySelector("#locations").value
    let data = await fetchData(`${BASE_URL}/${typeOfData}/${location}`);
    printData(data["data"]);
}

function printData(data) {
    let responseBody = document.querySelector("#answer tbody");
    responseBody.innerHTML = "";
    for (let item of data) {
        let tr = document.createElement("tr");
        for (let field in item) {
            let td = document.createElement("td");
            td.innerHTML = item[field];
            tr.appendChild(td);
        }
        responseBody.appendChild(tr);
    }
}