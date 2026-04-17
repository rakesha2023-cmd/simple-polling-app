
from flask import Flask, request, render_template

app = Flask(__name__)

poll = {"question": "", "options": []}

@app.route("/", methods=["GET", "POST"])
def create_poll():
    if request.method == "POST":
        poll["question"] = request.form["question"]
        poll["options"] = request.form.getlist("options")
    return render_template("create.html", poll=poll)

if __name__ == "__main__":
    app.run(port=5001)
