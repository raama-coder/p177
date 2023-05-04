from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs": 5,
        "category": "Board Games",
        "word": "Chess"
    },
    {
        "inputs": 6,
        "category": "European Country Name",
        "word": "France"
    },
    {
        "inputs": 7,
        "category":"Sports",
        "word":"Cricket"
    },
    {
        "inputs": 5,
        "category":"Italian Food",
        "word":"Pizza"
},
{
    "inputs": 5,
    "category":"Vehicle",
    "word":"Truck"
},
{
    "inputs": 8,
    "category":"Sports",
    "word":"FootBall"
}
]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()
