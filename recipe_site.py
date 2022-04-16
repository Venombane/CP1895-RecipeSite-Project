from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("mainPage.html")

@app.route("/addRecipe")
def add_recipe():
    bicycle_images = ["Alice", "Bob", "Charlie"]
    return render_template("addRecipe.html", bicycle_images=bicycle_images)

@app.route("/recipeList")
def recipes():
    bicycle_images = ["Alice", "Bob", "Charlie"]
    return render_template("recipeList.html", bicycle_images=bicycle_images)

@app.route("/removeRecipe")
def remove_recipe():
    bicycle_images = ["Alice", "Bob", "Charlie"]
    return render_template("removeRecipe.html", bicycle_images=bicycle_images)