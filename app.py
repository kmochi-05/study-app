from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("study.db")
    c = conn.cursor()

    c.execute("SELECT id, subject, time, date FROM records")
    records = c.fetchall()

    c.execute("SELECT SUM(time) FROM records")
    total = c.fetchone()[0]

    conn.close()

    return render_template("index.html", records=records, total = total)

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

    return redirect(url_for("home"))


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

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    conn = sqlite3.connect("study.db")
    c =conn.cursor()

    c.execute("DELETE FROM records WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
