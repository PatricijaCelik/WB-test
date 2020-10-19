import datetime

from flask import Flask, render_template

app = Flask(__name__)

# Template engine
# - IF statements, FOR loops, blocks (chaining of templates)
# - NO BUSINESS LOGIC

@app.route("/")
def index():
    name = "Patricija"
    cities = ["Ljubljana", "Maribor", "Rome", "Vienna", "Stockholm"]
    # cities = None - triggers if statement (cities are not shown)
    year = datetime.datetime.now().year
    return render_template("index.html", name=name, cities=cities, year=year)


@app.route("/about")
def about_me():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
