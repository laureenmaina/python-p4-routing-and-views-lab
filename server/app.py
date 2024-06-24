from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Python Operations with Flask Routing and Views </h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):

    print(parameter)

    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers=list(range(parameter))

    numbers_str = '\n'.join(map(str, numbers))

    return numbers_str.replace("\n", "<br>")

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):

    if operation=='+':
        result= num1+num2

    elif operation=='-':
        result= num1-num2

    elif operation=='*':
        result= num1*num2

    elif operation=='div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero", 400
        
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Error: Modulus by zero", 400
    else:
        return "Error: Unsupported operation", 400
    
    return str(result)
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
