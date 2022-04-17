"use strict"

const $ = selector => document.querySelector(selector);

const processEntries = () => {

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