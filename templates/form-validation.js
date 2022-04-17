"use strict"

const $ = selector => document.querySelector(selector);

const processEntries = () => {
    const recipe_name = $("#recipe-name");
    const servings = $("#servings");
    const total_time = $("#total-time");
    const prep_time = $("#prep-time");
    const description = $("#description");
    const ingredients = $("#ingredients");
    const instructions = $("#instructions");

    let isValid = true;
    if (recipe_name.value === "") {
        alert("Recipe name is required");
        isValid = false;
    }
    if (servings.value === "") {
        alert("Servings are required");
        isValid = false;
    } else if (isNaN(servings.value) === true) {
        alert("Servings must be a number.");
        isValid = false;
    }

    if (total_time.value === "") {
        alert("Total is required.");
        isValid = false;
    } else if (isNaN(total_time.value) === true) {
        alert("Total must be a number.");
        isValid = false;
    }

    if (prep_time.value === "") {
        alert("Prep time is required");
        isValid = false;
    } else if (isNaN(prep_time.value) === true) {
        alert("Prep time must be a number.");
        isValid = false;
    }

    if (description.value === "") {
        alert("Description is required");
        isValid = false;
    }
    if (ingredients.value === "") {
        alert("Ingredients are required");
        isValid = false;
    }
    if (instructions.value === "") {
        alert("Instructions are required");
        isValid = false;
    }

    if (isValid === true) {

        $("form").submit();
    }
};

const resetForm = () => {
    $('form').reset();
    $("#recipe-name").nextElementSibling.textContent = "*";
    $("#servings").nextElementSibling.textContent = "*";
    $("#total-time").nextElementSibling.textContent = "*";
    $("#prep-time").nextElementSibling.textContent = "*";
    $("#description").nextElementSibling.textContent = "*";
    $("#ingredients").nextElementSibling.textContent = "*";
    $("#instructions").nextElementSibling.textContent = "*";
    $("#recipe-name").focus();
}

document.addEventListener("DOMContentLoaded", () => {
    $("#submit").addEventListener("click", processEntries);
    $("#clear").addEventListener("click", resetForm);
    $("#recipe-name").focus();
});