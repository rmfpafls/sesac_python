# --------------------------------------------
# 1. os 활용 예제 
# 
# 1) os 디렉토리 구조 출력해보기 
# 2) root directory 아래에 있는 특정 확정자 파일들 다 출력하기 
# 3) os 디렉토리 복사하기 
# --------------------------------------------
import os 

root = r'C:\Users\user\Desktop\python_camp'

## 자 봐바 하위 폴더면 root 뒤에 \ 에 뭐가 더 붙을거야 
# 파일이면 .어쩌구 가 없다 

def print_directory_tree(root): 
    # 1) os 디렉토리 구조 출력해보기 
    file_list = []

    for elem in os.listdir(root): ##폴더가 아닌 파일 출력 
        if elem == elem.split('.')[-1]:
            file_list.append(elem)         
        else: 
            print(elem)

    if len(file_list) == 0:
        print("")
        return
    else:  
        for i in file_list:
            new_root = os.path.join(root, i)
            print(f"{new_root}이거 안에는")
            print_directory_tree(new_root)

print_directory_tree(root)

# 2) root directory 아래에 있는 특정 확정자 파일들 다 출력하기 
def list_extension_files(root):
    if os.path.isdir(elem):
        print('<DIR>\t\t' + elem)
    elif '.' in elem:
        extension = elem.split('.')[-1]
        print(f'{extension} file \t\t{elem}')

# 3) os 디렉토리 복사하기

def copy_directory(src, dest): #src의 내용을 dest에 복사한다.
    if os.path.exists(src):
        # 새로운 디렉토리 생성
        os.makedirs(dest, exist_ok=True)
        
        # 새로운 파일 경로 설정
        new_file_path = os.path.join(dest, os.path.basename(src))
        
        # 파일 내용 복사
        with open(src, 'r') as src_file:
            content = src_file.read()
        
        with open(new_file_path, 'w') as dest_file:
            dest_file.write(content)
        
        print(f"File '{src}' copied to '{new_file_path}'.")
    else: 
        print(f"{src} does not exist.")

copy_directory('example.txt', 'dest_dir')