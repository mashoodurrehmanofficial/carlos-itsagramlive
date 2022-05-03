from flask import jsonify,Flask,request

try:
    from live_broadcast import generateResponseFile
except:
    from .live_broadcast import generateResponseFile

app = Flask(__name__)


@app.route("/")
def index(): 
    print("--",request.data)
    return jsonify({})


@app.route("/getDataFile",methods = ['POST'])
def postAPIView(): 
    content = request.get_json(silent=True)

    username = str(content.get("username"))
    password = str(content.get("password"))
    data = generateResponseFile(username=username,password=password)
     
    print("Response = ",data)
     
    return jsonify(data)




app.run(host='0.0.0.0', port=8000,debug=True)
