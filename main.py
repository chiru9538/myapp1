from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():
    # return "Hello, World"
    return render_template("home.html")

@app.route("/PredictDefectORnot")
def PredictDefectORnot():
    return render_template("PredictDefectORnot.html")

@app.route("/ClassificationOfCases")
def ClassificationOfCases():
    return render_template("ClassificationOfCases.html")

if __name__ == "__main__":
    app.run(debug=True)
