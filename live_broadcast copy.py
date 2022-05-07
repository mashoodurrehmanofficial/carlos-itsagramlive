import sys,json, os 
dir_path = os.path.dirname(os.path.realpath(__file__))
from ItsAGramLive import ItsAGramLive

def generateResponseFile(username='',password='',file_path='',new_request_status_file_path=''):
    # live = ItsAGramLive( username=username,  password=password,)
    print("api called")
    live = ItsAGramLive(
        username='_fronji',
        password='81216163Xx_'
    )

    try:
        res = live.start(file_path=file_path,new_request_status_file_path=new_request_status_file_path) 
    except:
        res = {}
    return res

if __name__ == '__main__':
    generateResponseFile('_fronji','81216163Xx_')