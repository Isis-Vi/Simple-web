from flask import Flask

app = Flask(__name__)

@app.route("/")  #ruta raíz
def hello_world():
    return '<a href="whatever"> Go to the next route!</a>'

@app.route("/whatever")  #ruta hija num 1
def whenever():
    return "<h1>Bienvenidos Lol</h1>"
app.run(debug=True)