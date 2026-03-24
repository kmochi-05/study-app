from flask import Flask, render_template, request
import sqlite3

def init_db():
    conn = sqlite3.connect("study.db")
    c = conn.cursor()

    c.execute(""""
              CREATE TABLE IF NOT EXISTS records (
              id INTEGER PRIMARY KEY AUTOINCREMENT, 
              subject TEXT
              time INTGER,
              date TEXT
              )
              """)
    
    conn.commit()
    conn.close()


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    subject = request.form["subject"]
    time = request.form["time"]
    date = request.form["date"]

    conn = sqlite3.connect("study.db")
    c = conn.cursor()

    c.execute("INSERT INTO records (subject, time, date) VALUES (?, ?, ?)",
              (subject, time, date))
    
    conn.commit()
    conn.close()

    return "保存しました"

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
