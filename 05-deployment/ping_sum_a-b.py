from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    number1 = data.get('number1')
    number2 = data.get('number2')
    if number1 is not None and number2 is not None:
        result = number1 + number2
        return jsonify({'sum': result}), 200
    else:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)