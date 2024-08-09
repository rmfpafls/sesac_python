import pickle 

# pickle.load와 pickle.dump을 사용하지 않고 대체하는 함수 짜보기
# pickle.load : 파일을 읽어오겠다 

def safe_load(pickle_path):
    return pickle.load(open(pickle_path, 'rb'))
    

def safe_dump(pickle_path):
    d = {} 
    return pickle.dump(d,open(pickle_path, 'wb+'))


# --------------------------------------------
# 4. 합성함수 (추후 decorator)
# 
# 1) 만약 result.txt 파일이 없다면, 함수의 리턴값을 result.txt 파일에 출력하고, 만약 있다면 파일 내용을 읽어서 
#    '함수를 실행하지 않고' 리턴하게 하는 함수 cache_to_txt를 만들 것. txt 파일은 pickle_cache 폴더 밑에 만들 것.  
# 2) 함수의 실행값을 input에 따라 pickle에 저장하고, 있다면 pickle.load를 통해 읽어오고 없다면 
#    실행 후 pickle.dump를 통해 저장하게 하는 함수 cache_to_pickle을 만들 것. pickle 파일은 pickle_cache 폴더 밑에 만들 것. 
# 3) 함수의 실행값을 함수의 이름과 input에 따라 pickle에 저장하고, 2)와 비슷하게 진행할 것. pickle 파일은 pickle_cache 폴더 밑에, 각 함수의 이름을 따서 만들 것 
# --------------------------------------------
# level 2 
import os

def cache_to_txt(function): 

    def create_dir(directory_name): #디렉토리가 있는지 검색하고 없으면 새로 만들고, 있으면 안만드는 함수 
        if not os.path.exists(directory_name):
            print(f'{directory_name} dose not exists;')
            os.makedirs(directory_name)
        else: 
            print(f"{directory_name} dose exists")
    
    path =  r'pickle_cache'
    create_dir(path)

    if not os.path.exists(f"{path}/result.txt"): # 파일이 없다면, 함수의 리턴값을 result.txt에 출력
        res = function()
        f = open(f'{path}/result.txt', 'w+', encoding= 'utf-8')

        print(res, file = f)
        f.close()
    else: # 파일이 있다면 파일 내용을 읽어서 리턴 
        f = open('result.txt','r', encoding = 'utf-8')
        res = f.read()
        f.close()
        return res 

cache_to_txt(function = lambda : 'hello world')
