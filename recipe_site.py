import csv

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("mainPage.html")


@app.route("/addRecipe", methods=['POST', 'GET'])
def add_recipe():
    if request.method == 'POST':
        recipeName = request.form["recipe_name"]
        servings = request.form['servings']
        total = request.form['total_time']
        prep = request.form['prep_time']
        description = request.form['description']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        recipe = [recipeName, servings, total, prep, description, ingredients, instructions]

        with open('Recipes.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(recipe)
        return render_template("recipeList.html")

    else:
        return render_template("addRecipe.html")


@app.route("/recipeList")
def recipes():
    return render_template("recipeList.html")


@app.route("/removeRecipe")
def remove_recipe():
    return render_template("removeRecipe.html")