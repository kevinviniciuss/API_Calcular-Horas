from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

Horas_Trabalho = 5

@app.route('/')
def index():
    return render_template('index.html', resultado = None)

@app.route('/calcular', methods = ['POST'])
def calcular():
    entrada = request.form['entrada']
    saida = request.form['saida']

    try:
        formato = "%H:%M"
        hora_entrada = datetime.strptime(entrada, formato)
        hora_saida = datetime.strptime(saida, formato)

        horas_trabalhadas = (hora_saida - hora_entrada).seconds / 3600

        diferenca = round(horas_trabalhadas - Horas_Trabalho, 2)

    except ValueError:
        return render_template('index.html', resultado="❌ Formato inválido! Use HH:MM (ex: 08:30)")