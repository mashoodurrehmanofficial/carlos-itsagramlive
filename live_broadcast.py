import sys,json, os 
dir_path = os.path.dirname(os.path.realpath(__file__))
from ItsAGramLive import ItsAGramLive

def generateResponseFile(username='',password=''):
    live = ItsAGramLive( username=username,  password=password,)

    # live = ItsAGramLive(
    #     username='_fronji',
    #     password='81216163Xx_'
    # )

    try:
        res = live.start(execute_all=False)
        print(res)
        with open(os.path.join(dir_path,"response.json"),'w',encoding="utf-8") as file:
            json.dump(res,file, indent=4)
    except:
        res = {}
    return res

if __name__ == '__main__':
    generateResponseFile()