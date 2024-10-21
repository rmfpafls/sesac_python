import glob 

def load_file(): 
    file = glob.glob(r'C:\Users\user\Desktop\seq2seq_실습\eng-fra.txt')
    print(file)