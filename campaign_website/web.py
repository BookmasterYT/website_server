from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/about/policy")
def policy():
    return render_template("policy.html")

@app.route("/about/support")
def support():
    return render_template("support.html")

@app.route("/resources/constitution")
def constitution():
    return render_template("constitution.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")