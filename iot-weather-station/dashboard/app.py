from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data")
def data():
    return jsonify({
        "temperature": round(random.uniform(25, 35), 2),
        "humidity": round(random.uniform(40, 60), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
