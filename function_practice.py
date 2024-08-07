import random 
lst= [4,6,7,1,3,5]

# --------------------------------------------
# 1. max / min 구현하기 
#
# cmp라는 함수를 이용한 min/max 구현하기. 
# cmp는 두 원소 중 더 큰 것을 반환하는 함수. 
# --------------------------------------------

def my_max(lst, cmp = lambda x, y: x):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if cmp(lst[i],lst[j]) == lst[i]:
                lst[i], lst[j] = lst[j], lst[i] 
    return lst
print(my_max(lst)[-1])

def my_min(lst, cmp = lambda x, y: x):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if cmp(lst[i],lst[j]) == lst[i]:
                lst[i], lst[j] = lst[j], lst[i] 
    return lst
print(my_max(lst)[])
# --------------------------------------------
# 2. sort 구현하기 
# 
# 1) 그냥 순서대로 오름차순으로 정렬하기 
# 2) 오름차순, 내림차순으로 정렬하기 
# 3) 주어진 기준 cmp에 맞춰서 오름차순, 내림차순으로 정렬하기 
# 4) 주어진 기준 cmp가 큰 element를 출력하거나, 같다는 결과를 출력하게 만들기   
# 5) cmp상 같은 경우 tie-breaking하는 함수 넣기  # tie-breaking이 뭐에요...? 
# --------------------------------------------


def sort1(lst): # 1) 그냥 순서대로 오름차순으로 정렬하기 
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

print(sort1(lst)) 
                
def sort2(lst, upper_to_lower = True): # 2) 오름차순, 내림차순으로 정렬하기 
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i] 
    if upper_to_lower == True: # 오름차순 
        return print(lst)
    else:# 내림차순  
        return print(lst[::-1])
 
print(sort2(lst))

# 3) 주어진 기준 cmp에 맞춰서 오름차순, 내림차순으로 정렬하기 
def sort3(lst, upper_to_lower = True, cmp = lambda x, y: x):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if cmp(lst[i],lst[j]) == lst[i]:
                lst[i], lst[j] = lst[j], lst[i] 

    if not upper_to_lower: # 오름차순 
        print(lst)
        return 
    else:# 내림차순 
        print(lst[::-1]) 
        return 

sort3(lst,upper_to_lower = True, cmp = lambda x, y: x if len(x)>len(y) else y) 

# if 긴게 최고다 긴게 제일 큰 값이다
# Q.호출 할때 인자에 cmp = lambda x, y: x if len(x)>len(y) else y 넣어야되나요???? 
# 넵, 모든 형태를 맞춰서 써야됩니다~

# 4) 주어진 기준 cmp가 큰 element를 출력하거나, 같다는 결과를 출력하게 만들기
def sort4(lst, upper_to_lower = True, cmp = lambda x, y: x):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if cmp(lst[i],lst[j]) == lst[i]:
                lst[i], lst[j] = lst[j], lst[i] 

    if cmp(lst[-1],lst[-2]) == lst[-2] and cmp(lst[-2],lst[-1]) == lst[-1]:
        print(f'{lst[-1]}는 {lst[-2]}와 같습니다. ')
        return         
    elif not upper_to_lower: # 오름차순 
        print(lst[-1])
        return 
    else:# 내림차순 
        print(lst[::-1][-1]) 
        return 

sort4(lst,upper_to_lower = False, cmp = lambda x, y: x if len(x)>len(y) else y)

# 5) cmp상 같은 경우 tie-breaking하는 함수 넣기  # tie-breaking이 뭐에요...? 
def sort5(lst, upper_to_lower = True, cmp = lambda x, y: x, tie_breaker = lambda x, y: random.choice([x,y])):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if cmp(lst[i],lst[j]) == lst[i]:
                lst[i], lst[j] = lst[j], lst[i] 

    if cmp(lst[-1],lst[-2]) == lst[-2] and cmp(lst[-2],lst[-1]) == lst[-1]:
        print(tie_breaker(lst[-1],lst[-2]))
        return         
    elif upper_to_lower: # 오름차순 
        print(lst[-1])
        return 
    else:# 내림차순 
        print(lst[::-1][-1]) 
        return     


sort5(lst, upper_to_lower = True, cmp = lambda x, y:  x if len(x)>len(y) else y, tie_breaker = lambda x, y: random.choice([x,y]))



# --------------------------------------------
# os_file_concept.py 해보고 올 것 
# --------------------------------------------

# --------------------------------------------
# 3. safe pickle load/dump 만들기 
# 
# 일반적으로 pickle.load를 하면 무조건 파일을 읽어와야 하고, dump는 써야하는데 반대로 하면 굉장히 피곤해진다. 
# 이런 부분에서 pickle.load와 pickle.dump를 대체하는 함수 safe_load, safe_dump를 짜 볼 것.  
# hint. 말만 어렵고 문제 자체는 정말 쉬운 함수임. 거짓말...강사님만 쉬운거면서....
# --------------------------------------------

# return에 있는 값을 쓸 때마다 치면 뒤에 모드를 잘못 써서 전에 작업한걸 다 날릴 수도 있으니까
# 함수로 지정해둬서 모드로 인한 이슈를 방지하는거임 

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


def cache_to_pickle(function):

    def res(*arg, **kargs):  # res(1)
        def create_dir(directory_name): #디렉토리가 있는지 검색하고 없으면 새로 만들고, 있으면 안만드는 함수 
            if not os.path.exists(directory_name):
                print(f'{directory_name} dose not exists;')
                os.makedirs(directory_name)
            else: 
                print(f"{directory_name} dose exists")
        
        path =  r'pickle_cache'

        create_dir(path)

        # print(arg[0]) # 1

        # for i in arg: 
        #     print(function(i)) #하면 출력 2나옴 !!!!!

        if not os.path.exists(f'{path}/{arg}.pickle'): # 파일이 없다면 함수 실행 후 puck.dump를 통해 저장하고
            jar = function(*arg, **kargs)# input에 따라 pickle에 저장
            print(f"\n파일없어서 \n\n{jar} \n\n이거 저장할게요.")
            pickle.dump(jar, open(f'{path}/{arg}.pickle', 'wb+'))
            return jar 
            
        else: # 파일이 있다면 pickle.load를 통해 읽어오자
            # 없다면 새로만드는거고  f(2)
            bottle = pickle.load(open(f'{path}/{arg}.pickle', 'rb'))
            print("파일있어요\n",bottle)

            return bottle 
    
    return res         

def double(x, y): return 2*(x+y)

(cache_to_pickle(double)(2, 3))


