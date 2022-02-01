from flask import Flask, render_template, request, jsonify,redirect,url_for
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST',"GET"])
@cross_origin()
def say_name():
    data=request.form.get("txt1")
    try:
        data=data.split(":")
    except:
        return render_template('index.html')

    try:
        print(data)
        print("https://www.google.com/maps/@"+data[0]+","+data[1])
        print("Accuracy: ",data[2])
        print('here')
        return render_template('index.html')
        
    except:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
