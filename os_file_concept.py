import os 
import pickle 

# --------------------------------------------
# 1. os 기초 예제 
# 
# 1) os.path 이해하기 (os.path.exists, os.path.join, os.path)
# 2) os.listdir / os.makedir 해보기 
# 3) os.getcwd / os.changedir 해보기 
# --------------------------------------------

print(os.getcwd()) #현재 위치 출력 

for elem in os.listdir():
    # print(elem)
    if os.path.isdir(elem):
        print('<DIR>\t\t' + elem)
    elif '.' in elem:
        extension = elem.split('.')[-1]
        print(f'{extension} file \t\t{elem}')

def create_dir(directory_name): #디렉토리가 있는지 검색하고 없으면 새로 만들고 있으면 안만드는 함수 
    if not os.path.exists(directory_name):
        print(f'{directory_name} dose not exists;')
        os.makedirs(directory_name)
    else: 
        print(f"{directory_name} dose exists")

create_dir('hello world')

# --------------------------------------------
# 2. file 기초 예제 
# 
# 1) open 이해하기 
# 2) 파일 읽기, 써보기 
# --------------------------------------------
from time import time #실행되는데 걸리는 시간을 알고 싶다면 

begin = time()

f = open('example.txt', 'r', encoding = 'utf-8') 
# w모드는 기존에 있던 내용을 무조건 다 날려버리고 새로운 내용을 쓴다. 
# r모드는 읽기 모드 

print(f.readlines())
print(f.readlines())
for line in f.readlines():
    print(line)

#파일도 열었으면 언젠가는 닫아줘야돼요
f.close() 

end = time()
print(f"{end-begin} sec passed for coding")
# --------------------------------------------
# 3. pickle 기초 예제 
# 
# 1) pickle.load() 해보기 
# 2) pickle.dump() 해보기 
# --------------------------------------------

d = {}

k = pickle.dump(d, open('empty_dict.pickle', 'wb+')) 
# b의 의미 : 0과 1로만 이루어진 바이트로 저장하겠다는 의미
# 피클 절이듯 절여서 저장해놓고 나중에 쓰겠다~
# ㄹㅇ피클색이네 귀여워~~
print('this one',k)

e = pickle.load(open('empty_dict.pickle', 'rb'))# 파일을 읽어와서 e에 넣겠다.

print(e)