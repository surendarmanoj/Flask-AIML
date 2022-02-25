from urllib import response
from flask import Flask, render_template
import aiml
import os

kernel = aiml.Kernel()
for file in os.listdir("brain"):
    if file.endswith(".aiml"):
        kernel.learn("brain/" + file)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/<query>")
def homepage(query):
    return kernel.respond(query)

if __name__ == "__main__":
    app.run(debug=True)