import json
import os

MY_DATABASE = 'data'

def newfile(*param):
    with open(MY_DATABASE,'w') as wf:
     json.dump(param[0],wf,indent=4)

def AddData(*param):
   data =list(param)
   



   


