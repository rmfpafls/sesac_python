import glob 
import torch
import numpy as np 
from torch.utils.data import DataLoader, TensorDataset
from collections import defaultdict


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

def dict_vocab(sentences, voca, max_length): 
    """
    eng_voca : List : [(단어, 쓰인 횟수), ()]
    
    """
    word2idx = {} 
    idx2word = {}
    idx = 4

    word2idx['[PAD]'] = 0
    idx2word[0] = '[PAD]'

    word2idx['[SOS]'] = 1
    idx2word[1] = '[SOS]'

    word2idx['EOS'] = 2
    idx2word[2] = '[EOS]'

    word2idx['OOV'] = 3
    idx2word[3] = '[OOV]'

    for sentence in sentences: 
        for word in sentence: 
            for i in voca:
                if word not in word2idx:
                    if word in i[0]: 
                        word2idx[word] = idx
                        idx2word[idx] = word
                        idx += 1
    print(word2idx)
    return word2idx, idx2word

def threshold_word_voca(sentences, threshold = 0.99): 
    word_count_list = []
    vocab_dict = defaultdict(int)
    word_total_count = 0
    sorted_count = 0 

    for sentence in sentences: 
        for word in sentence: 
            vocab_dict[word.lower()] += 1
            word_total_count += 1

    sorted_lst = sorted(vocab_dict.items(), key = lambda item: item[1], reverse = True)
    word_total_count = word_total_count * threshold

    for i in sorted_lst: #[('word', word_count)]
        if sorted_count < word_total_count: 
            word_count_list.append(i)
            sorted_count += i[1]   

    return word_count_list

def determine_max_sentence(sentences, threshold = 0.99): 
    # eng_max_length = determine_max_sentence(eng_sentences)
    lst = []
    word_count_dict = defaultdict(int)
    total_sentence_length = 0
    sentence_count = 0 

    for sentence in sentences: 
        count = len(sentence)
        word_count_dict[count] += 1
        total_sentence_length += count 

    
    sorted_lst = sorted(word_count_dict.items(), key = lambda x: x[1], reverse=True)
    total_sentence_length = total_sentence_length*threshold

    for i in sorted_lst: 
        if sentence_count < total_sentence_length:
            sentence_count += i[1]
            lst.append(i)
    max_length = max(word_count_dict.items(), key = lambda x: x[0])
    # print(max_length[0]) # eng : 47, fra : 54
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
    eng_sentences, fra_sentences = load_file() # eng_sentences = [['word','word','word']. []]

    eng_voca = threshold_word_voca(eng_sentences, threshold = 0.99) # [(word, word_count), ()]
    fra_voca = threshold_word_voca(fra_sentences, threshold = 0.99)

    eng_max_length = determine_max_sentence(eng_sentences) # 36
    fra_max_length = determine_max_sentence(fra_sentences) # 39

    eng_word2idx, eng_idx2word = dict_vocab(eng_sentences, eng_voca, eng_max_length) # 47
    fra_word2idx, fra_idx2word = dict_vocab(fra_sentences, eng_voca, eng_max_length) # 54
    return 
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

    return train_dataloader, valid_dataloader, test_dataloader, eng_max_length, fra_max_length, eng_word2idx, fra_word2idx, eng_idx2word, fra_idx2word, eng_idx_sentence, fra_idx_sentence


