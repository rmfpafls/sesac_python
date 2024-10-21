import torch
from torch.utils.data import DataLoader, TensorDataset
import numpy as  np

def ffn_dataset(x,y,batch_size): 
    x = np.array(x)
    x = x.reshape(20074,384)
    x = x.tolist()

    train_x, train_y, valid_x, valid_y, test_x, test_y = split_train_valid_test(x,y)

    train_x = torch.stack([torch.tensor(item) for item in train_x])
    train_y = torch.tensor(train_y)  
    valid_x = torch.stack([torch.tensor(item) for item in valid_x])
    valid_y = torch.tensor(valid_y) 
    test_x = torch.stack([torch.tensor(item) for item in test_x])
    test_y = torch.tensor(test_y) 

    train_dataset = TensorDataset(train_x, train_y)
    valid_dataset = TensorDataset(valid_x, valid_y)
    test_dataset = TensorDataset(test_x, test_y)

    train_dataloader = DataLoader(train_dataset, batch_size = batch_size, shuffle= True)
    valid_dataloader = DataLoader(valid_dataset, batch_size = batch_size, shuffle= True)
    test_dataloader = DataLoader(test_dataset, batch_size = batch_size, shuffle = True)


    # for batch_x, batch_y in train_dataloader:
    #     print(batch_x.shape)  # (32, D) 형태
    #     print(batch_y.shape)  # (32,) 또는 (32, C) 형태

    return train_dataloader, valid_dataloader, test_dataloader


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