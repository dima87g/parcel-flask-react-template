from flask import Flask, render_template

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["JSON_AS_ASCII"] = False
app.config["ENV"] = "development"

@app.route("/")
def main():
    return render_template("index.html")

app.run(debug=True)
