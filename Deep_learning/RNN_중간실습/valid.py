import os 
import pickle 
import math
import torch

from evaluate import model_evaluate

def valid(model, valid_dataset, learning_rate, device): 
    loss_and_model_dict = pickle.load(open('loss_history.pkl', 'rb'))

    accuarcy_list = []
    best_accuarcy = 0
    
    for key in loss_and_model_dict.keys(): 
        accuarcy_list.append(key[2])

    for accuarcy in accuarcy_list: 
        if accuarcy > best_accuarcy: 
            best_accuarcy = accuarcy
    
    for key, value in loss_and_model_dict.items(): 
        print("key[2] :",key[2])
        print("best_accuarcy :", best_accuarcy)
        if key[2] == best_accuarcy:
            lr = key[0]
            model_state = loss_and_model_dict[(key[0], key[1], key[2])]
            model.load_state_dict(model_state)

    accuarcy, min_loss, file_path, pickle_loss_and_model, loss_list  = model_evaluate(model, valid_dataset, device, lr)
    print("valid_accuarcy :", accuarcy)
    print("valid_min_loss :", min_loss)
    
    return accuarcy, min_loss, model, lr, loss_list
