from flask import jsonify,Flask,request
import os,threading
from concurrent.futures import ThreadPoolExecutor
import sys,json, os 
dir_path = os.path.dirname(os.path.realpath(__file__))
from ItsAGramLive import ItsAGramLive

import time
dir_path = os.path.dirname(os.path.realpath(__file__))
response_file_path = os.path.join(dir_path,'response.json')
new_request_status_file_path = os.path.join(dir_path,'new_request.txt')


# try:
#     from live_broadcast import generateResponseFile
# except:
#     from .live_broadcast import generateResponseFile

def generateResponseFile(username='',password=''):
    
    live = ItsAGramLive( username=username,  password=password,)
    print("api called")
    # live = ItsAGramLive(
    #     username='_fronji',
    #     password='81216163Xx_'
    # )

    try:
        res = live.start(file_path=response_file_path,new_request_status_file_path=new_request_status_file_path) 
    except:
        res = {}
    return res

executor = ThreadPoolExecutor(1)



# my background thread
class MyWorker():

  def __init__(self, username,password):
    self.username = username
    self.password = password 

    thread = threading.Thread(target=generateResponseFile, args=(self.username,self.password))
    thread.daemon = True
    thread.start()

  def run(self):
    time.sleep(5)
    print("----00")

    # do something


app = Flask(__name__)


@app.route("/")
def index(): 
    print("--",request.data)
    return jsonify({})





        
@app.route("/getDataFile",methods = ['POST'])
def postAPIView(): 
    
    # updateStatusFile("1")
    
    
    content = request.get_json(silent=True) 
    username = str(content.get("username"))
    password = str(content.get("password"))
    
    if os.path.exists(response_file_path):
        os.remove(response_file_path)
    MyWorker(username,password)


    while not os.path.exists(response_file_path):
        time.sleep(0.1)
        print("-> waiting for res file")
    print('-> Created')
    print("thread finished...exiting") 

        
    with open(response_file_path,"r", encoding="utf-8") as file:
        return jsonify(json.loads(file.read()))
    return jsonify({})



# app.run(host='0.0.0.0', port=8000,debug=True)
