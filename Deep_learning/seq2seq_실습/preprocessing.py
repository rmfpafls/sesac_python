import glob 
import torch
import numpy as np 
from torch.utils.data import DataLoader, TensorDataset


def load_file(): 
    file = glob.glob(r'C:\Users\user\Desktop\seq2seq_실습\eng-fra.txt')[0]

    eng = []
    fran = []

    with open(file, encoding = 'utf-8') as f: 
        for line in f.readlines():
            expression = line.strip().split('\t')
            eng.append(expression[0])
            fran.append(expression[1])

    eng_token = []
    fra_token = []

    for eng_sentence in eng:
        split_sentence = eng_sentence.split()
        eng_token.append(split_sentence)

    for fra_sentence in fran: 
        split_sentence = fra_sentence.split()
        fra_token.append(split_sentence)

    return eng_token, fra_token 

def dict_vocab(sentences):
    word2idx = {} 
    idx2word = {}
    idx = 3

    word2idx['[PAD]'] = 0
    idx2word[0] = '[PAD]'

    word2idx['[SOS]'] = 1
    idx2word[1] = '[SOS]'

    word2idx['EOS'] = 2
    idx2word[2] = '[EOS]'

    for sentence in sentences: 
        for word in sentence: 
            if word not in word2idx: 
                word2idx[word] = idx
                idx2word[idx] = word
                idx += 1
    return word2idx, idx2word

def determine_max_sentence(token, threshold = 0.999): 
    max_length = 0

    for i in token: 
        length = len(i)

        if max_length < length: 
            max_length = length
    print(max_length)
    max_length = int(threshold*max_length)

    return max_length

def sentence2idx(sentences, word2idx, max_length): 
    res = []
    # print("max_length", max_length) # 46

    for sentence in sentences:
        elem_lst = []
        for word in sentence: 
            elem_lst.append(word2idx[word])
        lst = elem_lst + [0 for _ in range(max_length - len(elem_lst))]

        if len(lst) > max_length: 
            lst = lst[:max_length]
        res.append(lst)
    return res

def sentence2idx_with_tokens(sentences, word2idx, max_length): # max_length = 53
    res = []

    for sentence in sentences:
        elem_lst = [1]
        for word in sentence: 
            elem_lst.append(word2idx[word])
        elem_lst.append(2)
        lst = elem_lst + [0 for _ in range(max_length - len(elem_lst)+2)]

        if len(lst) > max_length+2: 
            lst = lst[:max_length+2]
        res.append(lst)
    return res

def split_train_valid_test(x, y, train_size = 0.8, valid_size = 0.1, test_size = 0.1): 
    data = []

    for i in range(len(x)): 
        data.append([x[i], y[i]])

    np.random.shuffle(data)

    train_max = int(len(x)*train_size)

    train_x = x[:train_max]
    train_y = y[:train_max]

    valid_max = int(train_max + len(x)*valid_size)

    valid_x = x[train_max:valid_max]
    valid_y = y[train_max:valid_max]

    test_x = x[valid_max:]
    test_y = y[valid_max:]
    
    return train_x, train_y, valid_x, valid_y, test_x, test_y    


def generate_dataset():  
    eng_sentences, fra_sentences = load_file() 

    eng_max_length = determine_max_sentence(eng_sentences) #46 => sos 46 eos => 48
    fra_max_length = determine_max_sentence(fra_sentences) #53

    eng_word2idx, eng_idx2word = dict_vocab(eng_sentences)
    fra_word2idx, fra_idx2word = dict_vocab(fra_sentences)

    eng_idx_sentence = sentence2idx(eng_sentences, eng_word2idx, eng_max_length) # [idx, pad]
    fra_idx_sentence = sentence2idx_with_tokens(fra_sentences, fra_word2idx, fra_max_length)

    # print("eng_idx_sentence :",  len(eng_idx_sentence)) # 135842
    # print("fra_idx_sentence :", len(fra_idx_sentence)) # 135842

    train_x, train_y, valid_x, valid_y, test_x, test_y = split_train_valid_test(eng_idx_sentence, fra_idx_sentence, train_size = 0.8, valid_size = 0.1, test_size = 0.1)

    train_x = torch.stack([torch.tensor(item) for item in train_x])
    train_y = torch.stack([torch.tensor(item) for item in train_y])  
    valid_x = torch.stack([torch.tensor(item) for item in valid_x])
    valid_y = torch.stack([torch.tensor(item) for item in valid_y]) 
    # for idx, item in enumerate(test_x): 
    #     print(torch.tensor(item).size()) # 진짜 맨 마지막꺼만 47임

    test_x = torch.stack([torch.tensor(item) for item in test_x]) ## 
    test_y = torch.stack([torch.tensor(item) for item in test_y]) 

    train_dataset = TensorDataset(train_x, train_y)
    valid_dataset = TensorDataset(valid_x, valid_y)
    test_dataset = TensorDataset(test_x, test_y)

    batch_size = 32

    train_dataloader = DataLoader(train_dataset, batch_size = batch_size, shuffle= True)
    valid_dataloader = DataLoader(valid_dataset, batch_size = batch_size, shuffle= True)
    test_dataloader = DataLoader(test_dataset, batch_size = batch_size, shuffle = True)

    return train_dataloader, valid_dataloader, test_dataloader


