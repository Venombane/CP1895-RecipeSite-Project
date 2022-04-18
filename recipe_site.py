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

        with open('Recipes.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(recipe)
            file.close()
        with open('Recipes.csv', 'r') as newFile:
            reader = csv.reader(newFile)
            add_recipes = list(reader)
            newFile.close()
        return render_template("recipeList.html", recipes=add_recipes)

    else:
        return render_template("addRecipe.html")


@app.route("/recipeList")
def recipes():
    with open('Recipes.csv', 'r') as file:
        reader = csv.reader(file)
        recipes = list(reader)
    return render_template("recipeList.html", recipes=recipes)


@app.route("/removeRecipe", methods=['POST', 'GET'])
def remove_recipe():
    with open('Recipes.csv', 'r') as file:
        reader = csv.reader(file)
        recipes = list(reader)
        file.close()
    if request.method == 'POST':
        recipe_number = request.form['recipe_number']

        if len(recipes) > int(recipe_number) > 0:
            recipes.pop(int(recipe_number) - 1)
            with open('Recipes.csv', 'w', newline='') as newFile:
                writer = csv.writer(newFile)
                for recipe in recipes:
                    writer.writerow(recipe)
                newFile.close()
            with open('Recipes.csv', 'r') as newFile:
                reader = csv.reader(newFile)
                add_recipes = list(reader)
                newFile.close()
            print("here")

            return render_template("recipeList.html", recipes=add_recipes)
        else:
            return render_template("recipeList.html", recipes=recipes)

    else:
        return render_template("removeRecipe.html", recipes=recipes)


@app.route("/remove_all_recipes", methods=['POST', 'GET'])
def remove_all_recipe():
    with open('Recipes.csv', 'r') as file:
        reader = csv.reader(file)
        recipes = list(reader)
        recipes.clear()
        with open('Recipes.csv', 'w') as newFile:
            writer = csv.writer(newFile)
            for recipe in recipes:
                writer.writerow(recipe)
        with open('Recipes.csv', 'r') as file:
            reader = csv.reader(file)
            new_recipes = list(reader)
            return render_template("recipeList.html", recipes=new_recipes)
