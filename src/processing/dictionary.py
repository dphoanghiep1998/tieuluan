import os
import json
import xml.etree.ElementTree as ET
import re
# module khoi tao dictionary
# trong dictionary co cac component(object)
# moi component gom text va` error text(cac loi thuong gap phai cua text)
# dict cac tu va loi cua no la 1 file text, chua cac dong`, moi dong` la

class Component: # class component, setup cho component
    def __init__(self,text,category,defi,error=None):
        self.text = text
        self.category = category
        self.error = error
        self.defi = defi
    def set_error(self,error):
        self.error = error


class Dictionary: # class dictionary, tao 1 class tu dien
    def __init__(self,words=None):
        self.words = words # words la cac list chua cac tu`
    
    def load(self,list_dir): # load file text -> dict(object)
        self.words = []
        for file in os.listdir(list_dir):
            tree = ET.parse(list_dir+"/"+file)
            root = tree.getroot()
            for entry in root.findall("Entry"):
                text = entry.find("HeadWord").text
                category = entry.find("Syntactic").find("Category").text
                defi = entry.find("Semantic").find("def").text
                com = Component(text,category,defi)
                self.words.append(com)


            
class DictionaryUtil:
    @staticmethod
    # co tu loi nao hay gap se dung ham nay de them vao
    def addError(dict):
        for word in dict.words:
            if(re.sub('ch','tr',word.text) != ""):
                error = re.sub('ch','tr',word.text)
                word.set_error(error)         
    

