
from flask import Flask, request, render_template

app = Flask(__name__)

poll = {"question": "Favorite Language?", "options": ["Python", "Java", "C++"], "votes": [0,0,0]}

@app.route("/", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        choice = int(request.form["option"])
        poll["votes"][choice] += 1
    return render_template("vote.html", poll=poll)

if __name__ == "__main__":
    app.run(port=5002)
