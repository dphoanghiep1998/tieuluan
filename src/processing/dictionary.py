import os
import json

# module khoi tao dictionary
# trong dictionary co cac component(object)
# moi component gom text va` error text(cac loi thuong gap phai cua text)
# dict cac tu va loi cua no la 1 file text, chua cac dong`, moi dong` la

class Component: # class component, setup cho component
    def __init__(self,text,error=None):
        self.text = text
        self.error = error
    def set_error(self,error):
        self.error = error


class Dictionary: # class dictionary, tao 1 class tu dien
    def __init__(self,words=None):
        self.words = words # words la cac list chua cac tu`
    
    def load(self,file_path): # load file text -> dict(object)
        self.words = []
        line  = [i.rstrip('\n') for i in open(file_path,encoding="utf8") if i.strip()]
        for content in line:
            item = json.loads(content)
            _lower_error = map(lambda x:x.lower(),item["error"])
            component = Component(item["text"].lower(),_lower_error)
            self.words.append(component)




