from flask import Flask,request,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!!!"

@app.route('/cal',methods=["GET"])
def math_op():
    operation = request.json["operation"]
    num1 = int(request.json["num1"])
    num2 = int(request.json["num2"])

    if operation == "add":
        result = num1+num2
    elif operation == "sub":
        result = num1 - num2
    else:
        result = num1 * num2

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
