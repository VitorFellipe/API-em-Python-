from flask import Flask
from datetime import date
app = Flask(__name__)

@app.route("/saudacao")
def datetoday():
    hoje = date.today()
    return f"hoje{hoje}"

if __name__ == "__main__":
    app.run(debug=True)