import torch
import random 
import numpy as np 
from torch.utils.data import DataLoader, TensorDataset
from collections import defaultdict

from load_file import load_file

OOV = '[OOV]'
PAD = '[PAD]'

def letter2tensor(letter, alphabets, oov = OOV):
    res = [0 for _ in range(len(alphabets))]

    if letter in alphabets:
        idx = alphabets.index(letter)
    else:
        idx = alphabets.index(oov)

    res[idx] = 1

    return torch.tensor(res)
    
def word2tensor(word, max_length, alphabets, pad = PAD, oov = OOV):
    res = torch.zeros(max_length, len(alphabets)) # 12 32

    for idx, char in enumerate(word): 
        if idx < max_length: 
            res[idx] = letter2tensor(char, alphabets, oov = oov)

    for i in range(max_length - len(word)): # padding 
        res[len(word)+i] = letter2tensor(pad, alphabets, oov = OOV)
    return res

def split_train_valid_test(x, y, train_size = 0.8, valid_size = 0.1, test_size = 0.1):
    
    train_max = int(len(x)*train_size)

    train_x = x[:train_max]
    train_y = y[:train_max]

    valid_max = int(train_max + len(x)*valid_size)


    valid_x = x[train_max:valid_max]
    valid_y = y[train_max:valid_max]

    test_x = x[valid_max:]
    test_y = y[valid_max:]

    return train_x, train_y, valid_x, valid_y, test_x, test_y 

def determine_alphabets(data, pad = PAD, oov = OOV, threshold = 0.999):
    lst = []
    character_dict = defaultdict(int)

    for name, lang in data: 
        for char in name: 
            character_dict[char.lower()] += 1 # 이거 알파벳이 아닌 글자에는 그대로 나오기 때문에 lower() 가능
            # chacter_dict : 각 문자당 사용된 횟수 

    for k, v in character_dict.items(): # k : 문자, v : 횟수
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

def determine_max_length(data, threshold = 0.99):
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
        if s > threshold * total_count: 
            return k -1 # threshole퍼센트 이상이면 그 전 단어 횟수만큼만 사용하겠다. 
        
    # return max(lst, key = lambda x:x[0]) # 제일 긴 단어 길이 - 이거 사용안하는데 왜 씀 


def generate_dataset(batch_size = 32, pad = PAD, oov = OOV):
    data, languages = load_file()
    alphabets = determine_alphabets(data, pad = pad, oov = oov) # 사용된 모든 단어+pad+oov
    max_length = determine_max_length(data) # 사용할 단어의 최대 길이 

    np.random.shuffle(data) #앞쪽 파일만 학습하는 걸 방지하려고 한번 섞음 

    for idx, elem in enumerate(data): # elem = [name, lang]
        tmp = []

        for char in elem[0]: 
            if char.lower() in alphabets: 
                tmp.append(char.lower())
            else: 
                tmp.append(oov)

        # data = [[name(lower, oov처리 끝), lang], 
        
        data[idx][0] = word2tensor(tmp, max_length, alphabets, pad = PAD, oov = OOV)
        data[idx][1] = languages.index(data[idx][1]) # languages를 인덱스 형태로 바꿈

    x = [e[0] for e in data]
    y = [torch.tensor(e[1]) for e in data] 

    return x,y, alphabets, max_length, languages, batch_size

    # train_x, train_y, valid_x, valid_y, test_x, test_y = split_train_valid_test(x,y)
    # # print(len(train_x)) # 16059

    # train_x = torch.stack(train_x)
    # train_y = torch.stack(train_y)
    # valid_x = torch.stack(valid_x)
    # valid_y = torch.stack(valid_y)
    # test_x = torch.stack(test_x)
    # test_y = torch.stack(test_y)

    # # print("train_x :", len(train_x) )

    # train_dataset = TensorDataset(train_x, train_y)
    # valid_dataset = TensorDataset(valid_x, valid_y)
    # test_dataset = TensorDataset(test_x, test_y)

    # # print("train_dataset : ", len(train_dataset))

    # train_dataloader = DataLoader(train_dataset, batch_size = batch_size, shuffle= True)
    # valid_dataloader = DataLoader(valid_dataset, batch_size = batch_size, shuffle= True)
    # test_dataloader = DataLoader(test_dataset, batch_size = batch_size, shuffle = True)


    # # for batch_x, batch_y in train_dataloader:
    # #     print(batch_x.shape)  # (32, D) 형태
    # #     print(batch_y.shape)  # (32,) 또는 (32, C) 형태

    # return train_dataloader, valid_dataloader, test_dataloader, alphabets, max_length, languages

 