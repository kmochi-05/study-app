from flask import Flask, render_template, request, redirect
import sqlite3

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

    return redirect("/")


def init_db():
    conn = sqlite3.connect("study.db")
    c = conn.cursor()

    c.execute("""
              CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                subject TEXT,
                time INTEGER,
                date TEXT
                )
              """)
    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
