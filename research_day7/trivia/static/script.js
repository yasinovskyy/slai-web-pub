"use strict";

let number = [1, 5, 10]
let area = { 9: "General knowledge", 20: "Mythology", 22: "Geography", 23: "History" }

function populateSelect(selectElementId, options) {
    // TODO :Implement this function
    let selectElement = document.querySelector(selectElementId);
    for (let key in options) {
        let newOption = document.createElement("option");
        newOption.setAttribute("value", key);
        newOption.innerText = options[key];
        selectElement.appendChild(newOption);
    }
}

async function getQuestions() {
    // TODO :Implement this function
    let chosenNumber = document.querySelector("#numberSelect").value;
    let chosenArea = document.querySelector("#areaSelect").value;
    let questions = await getData(chosenNumber, chosenArea);
    let questionSection = document.querySelector("#questions");
    console.log(questions["results"]);
    displayQuestion(questionSection, questions["results"], 0);

}

async function getData(chosenNumber, chosenArea) {
    // TODO :Implement this function
    let url = `https://opentdb.com/api.php?amount=${number[chosenNumber]}&category=${chosenArea}`;
    console.log(url);

    return fetch(url).then(response => response.json()).catch(error => console.log(error));
}

function displayQuestion(questionSection, questionPool, questionId) {
    questionSection.innerHTML = "";
    let questionCard = document.createElement("aside");
    questionCard.classList.add(questionPool[questionId]["difficulty"]);

    let questionText = document.createElement("h3");
    questionText.innerHTML = questionPool[questionId]["question"];
    questionCard.append(questionText);

    let answersList = document.createElement("ol");
    let answers = questionPool[questionId]["incorrect_answers"].slice();
    answers.push(questionPool[questionId]["correct_answer"]);
    answers.sort();

    for (let answer of answers) {
        let answerItem = document.createElement("li");
        answerItem.innerHTML = answer;
        answersList.append(answerItem);
    }
    questionCard.appendChild(answersList);

    let btnReveal = document.createElement("button");
    btnReveal.setAttribute("value", "reveal");
    btnReveal.innerText = "Reveal correct";
    questionCard.append(btnReveal);
    btnReveal.onclick = () => {
        for (let someAnswer of document.querySelectorAll("#questions li")) {
            if (someAnswer.innerHTML == questionPool[questionId]["correct_answer"]) {
                someAnswer.setAttribute("class", "correct_answer");
            }
        }
    }

    let btnNext = document.createElement("button");
    btnNext.setAttribute("value", "next");
    btnNext.classList.add("right");
    btnNext.innerText = "Show next";
    btnNext.onclick = () => {
        displayQuestion(questionSection, questionPool, (questionId + 1) % questionPool.length);
    }

    questionCard.append(btnNext);
    questionSection.append(questionCard);
}

window.onload = function () {
    this.populateSelect("#numberSelect", number);
    this.populateSelect("#areaSelect", area);
}