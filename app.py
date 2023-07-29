from flask import Flask,request,render_template

obj = Flask(__name__)

@obj.route('/')
def hello():
    return "Hello World!!!"

@obj.route('/cal',methods=["GET"])
def math_op():
    operation = request.json["operation"]
    num1 = request.json["num1"]
    num2 = request.json["num2"]

    if operation == "add":
        result = num1+num2
    elif operation == "sub":
        result = num1 - num2
    else:
        result = num1 * num2

    return result

if __name__ == '__main__':
    app.run(debug=True)
