from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("players") == None:
        session["players"] = []
    if request.method == "POST":
        player = request.form.get("player")
        session["players"].append(player)

    return render_template("home.html", players=session["players"])

if __name__ == "__main__":
    app.run(debug=True)