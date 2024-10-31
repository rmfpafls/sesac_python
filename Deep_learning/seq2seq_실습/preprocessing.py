import glob 
import torch
import numpy as np 
from torch.utils.data import DataLoader, TensorDataset
from collections import defaultdict

"""
max_length보다 긴 문장은 max_length만큼만 잘라서 eos 붙여준다음에 사용함
"""

def load_file(): 
    file = glob.glob(r'C:\Users\user\Desktop\seq2seq_실습\small_eng-fra.txt')[0]

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
    eng_word2idx, eng_idx2word = dict_vocab(eng_sentences, eng_voca, eng_max_length) 
    voca : List : [(단어, 쓰인 횟수), ()]
    
    """
    word2idx = {} 
    idx2word = {}
    idx = 4

    word2idx['[PAD]'] = 0
    idx2word[0] = '[PAD]'

    word2idx['[SOS]'] = 1
    idx2word[1] = '[SOS]'

    word2idx['[EOS]'] = 2
    idx2word[2] = '[EOS]'

    word2idx['[OOV]'] = 3
    idx2word[3] = '[OOV]'

    voca_dict = {word : count for word, count in voca}

    for sentence in sentences: # sentences : [['word','word','word'], ['word', 'word', 'word']]
        for word in sentence: 
                if word not in word2idx and word in voca_dict:
                        word2idx[word] = idx
                        idx2word[idx] = word
                        idx += 1
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
        total_sentence_length += 1

    
    sorted_lst = sorted(word_count_dict.items(), key = lambda x: x[0])
    # print(sorted_lst)
    # print("before total_sentence_length :", total_sentence_length)
    total_sentence_length = total_sentence_length*threshold # 134483.58
    # print("after total_sentence_length :", total_sentence_length) #  : 

    for i in sorted_lst: 
        if sentence_count < total_sentence_length:
            sentence_count += i[1]
            # print(sentence_count)
        else: 
            max_length = i[0]
            break
    return max_length

def sentence2idx(sentences, word2idx, max_length): #eng_idx_sentence = sentence2idx(eng_sentences, eng_word2idx, eng_max_length)
    res = []

    for sentence in sentences:
        elem_lst = []
        for word in sentence: 
            if word in word2idx: 
                elem_lst.append(word2idx[word])
            else: 
                elem_lst.append(3) #OOV
        lst = elem_lst + [0 for _ in range(max_length - len(elem_lst))]

        if len(lst) > max_length: 
            lst = lst[:max_length]
        res.append(lst)
    return res

def sentence2idx_with_tokens(sentences, word2idx, max_length): # fra_idx_sentence = sentence2idx_with_tokens(fra_sentences, fra_word2idx, fra_max_length)
    res = []

    for sentence in sentences:
        elem_lst = [1] #SOS
        for word in sentence: 
            if word in word2idx: 
                elem_lst.append(word2idx[word])
            else: 
                elem_lst.append(3) # OOV
        elem_lst.append(2) # EOS
        
        lst = elem_lst + [0 for _ in range(max_length - len(elem_lst)+2)]

        if len(lst) > max_length+2: 
            lst = lst[:max_length+2]
            if lst[-1] != 2: 
                lst[-1] = 2
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

    eng_voca = threshold_word_voca(eng_sentences, threshold = 0.99) # List : [(word, word_count), ()]
    fra_voca = threshold_word_voca(fra_sentences, threshold = 0.99)

    eng_max_length = determine_max_sentence(eng_sentences) # 15
    fra_max_length = determine_max_sentence(fra_sentences) # 17

    # print(len(eng_voca), len(fra_voca), eng_max_length, fra_max_length) # 1957 2380 37 49

    eng_word2idx, eng_idx2word = dict_vocab(eng_sentences, eng_voca, eng_max_length) # dict 
    fra_word2idx, fra_idx2word = dict_vocab(fra_sentences, fra_voca, fra_max_length) # dict 

    eng_idx_sentence = sentence2idx(eng_sentences, eng_word2idx, eng_max_length) # [idx, pad]
    fra_idx_sentence = sentence2idx_with_tokens(fra_sentences, fra_word2idx, fra_max_length)

    # print("eng_idx_sentence :",  eng_idx_sentence) # 135842
    # print("fra_idx_sentence :", len(fra_idx_sentence)) # 135842
    

    train_x, train_y, valid_x, valid_y, test_x, test_y = split_train_valid_test(eng_idx_sentence, fra_idx_sentence, train_size = 0.8, valid_size = 0.1, test_size = 0.1)

    train_x = torch.stack([torch.tensor(item) for item in train_x])
    # print(train_x.size()) # torch.Size([108673, 15])
    train_y = torch.stack([torch.tensor(item) for item in train_y])  
    valid_x = torch.stack([torch.tensor(item) for item in valid_x])
    valid_y = torch.stack([torch.tensor(item) for item in valid_y]) 

    test_x = torch.stack([torch.tensor(item) for item in test_x]) ## 
    test_y = torch.stack([torch.tensor(item) for item in test_y]) 

    train_dataset = TensorDataset(train_x, train_y)
    valid_dataset = TensorDataset(valid_x, valid_y)
    test_dataset = TensorDataset(test_x, test_y)

    batch_size = 32

    train_dataloader = DataLoader(train_dataset, batch_size = batch_size, shuffle= True)
    valid_dataloader = DataLoader(valid_dataset, batch_size = batch_size, shuffle= True)
    test_dataloader = DataLoader(test_dataset, batch_size = batch_size, shuffle = True)

    return train_dataloader, valid_dataloader, test_dataloader, eng_max_length, fra_max_length+2, eng_word2idx, fra_word2idx, eng_idx2word, fra_idx2word, eng_idx_sentence, fra_idx_sentence, eng_voca, fra_voca


