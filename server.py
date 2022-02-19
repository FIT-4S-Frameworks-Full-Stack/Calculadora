import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('calculadora.html')

@app.route('/calculaform', methods=['POST', 'GET'])
def calculaform():
    valor1 = request.form['v1']
    operacao = request.form['operacao']
    valor2 = request.form['v2']

    try:
        v1 = int(valor1)
    except ValueError:
        return "Erro!"

    try:
        v2 = int(valor2)
    except ValueError:
        return "Erro!"

    if (operacao == "soma"):
        resultadoCalculado = int(v1 + v2)
    elif (operacao == "subtracao"):
        resultadoCalculado = int(v1 - v2)
    elif (operacao == "divisao"):
        if (v2 == 0):
            return "Impossível dividir um número por zero."
        else:
            resultadoCalculado = int(v1 / v2)
    elif (operacao == "multiplicacao"):
        resultadoCalculado = int(v1 * v2)
    else:
        return "Erro!"

    return str(resultadoCalculado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='localhost', port=port)
