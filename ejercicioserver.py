# EJERCICIO

# POST -> localhost/order
# json -> {"numbers": [23, 432, 88, 90, 90, 70]} Números positivos del 1 al 1000, se pueden repetir.
# SIEMPRE SE RECIBE LISTA NUMERICA (no pasan strings, ni números negativos, y no se presupone que
# el usuario la va a liar.

# se pide:
# eliminar elementos repetidos
# ordenar de menor a mayor los restantes
# devolver en formato json:
# {"numbers":[0, 15, 89, 90, 90, 28, 36]}

from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/ejercicioserver', methods=['POST'])
def order():
    data = request.json
    numbers = data.get('numbers')
    numbers = list(set(numbers))
    #numbers.sort(reverse=True)
    #Con esta opcion se ordenan los numeros de mayor a menor
    numbers.sort(reverse=False)
    #Se establece reverse False porque en el ejercicio se indica que sea de menor a mayor.
    return jsonify(numbers)


app.run(host='0.0.0.0', port=80, debug=True)