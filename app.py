from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    subject = request.form["subject"]
    time = request.form["time"]
    date = request.form["date"]

    return f"科目: {subject}, 時間: {time}, 日付: {date}"

if __name__ == "__main__":
    app.run(debug=True)