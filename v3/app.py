
from flask import Flask, render_template

app = Flask(__name__)

poll = {"question": "Favorite Language?", "options": ["Python", "Java", "C++"], "votes": [5,3,2]}

@app.route("/")
def results():
    return render_template("results.html", poll=poll)

if __name__ == "__main__":
    app.run(port=5003)
