'''
pickle 파일 
 - 파이썬 객체(list, dict)를 이진파일(binary)로 저장
'''

# 1. file read 
path = r'C:\ITWILL\2_Python\workspace\chap08_FileIO\data' 
rfile = open(path + '/texts.txt', mode = 'r', encoding='utf-8')
texts = rfile.readlines()

# 2. word count 
words = [] # 단어 저장 
wc = {} # 단어 빈도수 
 
# word 추출 & word count 
for line in texts : # list
    for word in line.split() : # str
        words.append(word) # 단어 생성 
        wc[word] = wc.get(word, 0) + 1 # 단어 빈도수     

print(words) # list 
print(wc) # dict   

# 3. pickle save
import pickle 

dir(pickle) 
'''
dump(object, file) : 해당 객체를 이진파일로 저장 
load(file) : 해당 이진파일을 읽기   
''' 

# binary file save
file = open(path + '/wc_data.pickle', mode='wb') # 이진파일 
pickle.dump(wc, file) 
file.close()

# binary file load 
file = open(path + '/wc_data.pickle', mode='rb') # 이진파일
load_wc = pickle.load(file)

print(load_wc)
type(load_wc) # dict














