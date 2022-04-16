from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("mainPage.html")

@app.route("/album")
def album():
    bicycle_images = ["Alice", "Bob", "Charlie"]
    return render_template("index.html", bicycle_images=bicycle_images)