from dictionary import Dictionary
from dictionary import DictionaryUtil
import re

ft = DictionaryUtil()

dict = Dictionary()
dict.load("../xml")
ft.addError(dict)

# ham check input co thoa man luat ko ( test đầu tiên với luật có trong từ điển đã)
# để làm đc thì cần tokenizer
# có thể có chuẩn hóa

def check(input,dict):
    a = input.lower().split(" ")
    for word in dict.words:
        for i in range(len(a)-1):
            if(a[i]+" "+a[i+1]) in word.error:
                    for match in re.finditer(a[i]+" "+a[i+1],input):
                        print([(match.start(),match.end()),a[i]+" "+a[i+1]])
                    
def main():
    if input:
        check(input,dict)

if __name__ == "__main__":
    input = input()
    main()
