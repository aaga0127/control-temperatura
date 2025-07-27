
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return "Bienvenido a Control de Temperaturas - Alimentos de Mesoamérica"

if __name__ == '__main__':
    app.run()
