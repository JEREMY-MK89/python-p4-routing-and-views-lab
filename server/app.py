from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)  
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    result = '\n'.join(map(str, range(parameter + 1)))
    print(result)
    return result, 200



@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = str(int(num1) + int(num2))
    elif operation == '-':
        result = str(int(num1) - int(num2))
    elif operation == '*':
        result = str(int(num1) * int(num2))
    elif operation == 'div':
        result = str(int(num1) / int(num2))
    elif operation == '%':
        result = str(int(num1) % int(num2))
    
    if result is not None:
        return result, 200
    else:
        return '', 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
