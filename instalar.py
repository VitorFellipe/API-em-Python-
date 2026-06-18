from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Vitor Fellipe Kogiteski Magalhães da Silva Santos"

@app.route("/curso")
def curso():
    return "Desenvolvimento de Sistemas/Informatica"

@app.route("/escola")
def minhaescola():
    return "Ceep"
if __name__ == "__main__":
    app.run(debug=True)