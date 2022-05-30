from flask import Flask, request, render_template
import openai

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def monster_maker():
    error = None
    if request.method == "GET":
        return render_template("maker_form.html")
    elif request.method == "POST":
        openai.api_key = "CODE_HERE"
        completion = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Create a statblock for this D&D 5e monster \n" + request.form["monster_name"],
            max_tokens=1000
        )
        return completion["choices"][0]["text"]
    else:
        return "Test test test test test"


if __name__ == '__main__':
    app.run()
