from load_file import load_file
from collections import defaultdict


OOV = '[OOV]'
PAD = '[PAD]'

def determine_alphabets(data, pad = PAD, oov = OOV, threshold = 0.999):
    lst = []
    character_dict = defaultdict(int)

    for name, lang in data: 
        for char in name: 
            character_dict[char.lower()] += 1
    
    for k, v in character_dict.items(): 
        lst.append((k,v))

    lst = sorted(lst, key = lambda x: x[1], reverse = True)
    total_count = sum([e[1] for e in lst])

    s = 0
    alphabets = [] 

    for k, v in lst: 
        s += v 
        if s < threshold * total_count: 
            alphabets.append(k)
        
    alphabets.append(pad)
    alphabets.append(oov)

    return alphabets

def determine_max_length(data, threshole = 0.99):
    lst = []
    name_length_dict = defaultdict(int)

    for name, lang in data: 
        name_length_dict[len(name)] += 1

    for k, v in name_length_dict.items(): #{이름길이: 나오는 횟수 }
        lst.append((k,v))
    
    lst = sorted(lst, key = lambda x: x[1], reverse = True)
    total_count = sum([e[1] for e in lst])
    s = 0

    for k, v in lst: 
        s += v
        if s > threshole * total_count: 
            return k -1 # threshole퍼센트 이상이면 그 전 단어 횟수만큼만 사용하겠다. 
        
    return max(lst, key = lambda x:x[0]) # 제일 긴 단어 길이 
    



def generate_dataset(batch_size = 32, pad = PAD, oov = OOV):
    data, languages = load_file()
    alphabets = determine_alphabets(data, pad = pad, oov = oov)
    max_length = determine_max_length(data)
    print(alphabets, max_length) 
