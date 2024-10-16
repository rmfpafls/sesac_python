import torch

def ffn_dataset(data, alphabets, max_length, languages): 
    x = [] 
    y = [] 

    for batch_x, batch_y in data:
        print("batch_x.size(0) :", batch_x.size(0))
        for i in range(batch_x.size(0)):
            x.append(batch_x[i].reshape((batch_x.size(1) * batch_x.size(2))))
            y.append(batch_y[i])

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