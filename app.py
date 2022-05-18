from click import prompt
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)

app.config["SECRET_KEY"] = "chickensrcool1337"
debug = DebugToolbarExtension(app)


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
)


@app.route("/")
def show_homepage():
    prompts = story.prompts
    return render_template("index.html", prompts=prompts)


@app.route("/story")
def show_stories():
    answers = request.args
    mad_lib = story.generate(answers)
    return render_template("story.html", mad_lib=mad_lib)
