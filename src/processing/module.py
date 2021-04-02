from dictionary import Dictionary

dict = Dictionary()
dict.load("../dictionary/dict.txt")

# ham check input co thoa man luat ko ( test đầu tiên với luật có trong từ điển đã)
# để làm đc thì cần tokenizer
# có thể có chuẩn hóa

def check(input,dict):
    a = input.lower().split()
    for i in range(0,len(a)-1):
        for word in dict.words:
            if((a[i]+" "+a[i+1]) in word.error):
                print(a[i]+" "+a[i+1])
                print("True")

def main():
    if input:
        check(input,dict)

if __name__ == "__main__":
    input = input()
    main()
    