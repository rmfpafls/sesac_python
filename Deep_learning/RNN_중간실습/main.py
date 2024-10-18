import torch
import torch.nn as nn 
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
from collections import defaultdict
from torch.utils.data import DataLoader, TensorDataset
import os 
import pickle

from preprocessing import generate_dataset
from modeling import FeedForwardNetwork 
from train import train_model, plot_model
from modify_ffn_dataset import ffn_dataset
from evaluate import model_evaluate, save_file
from valid import valid

device = torch.device("cpu")#  if torch.cuda.is_available() )

if __name__ == "__main__": 
    x,y, alphabets, max_length, languages, batch_size  = generate_dataset()
    train_dataloader, valid_dataloader, test_dataloader = ffn_dataset(x,y, batch_size)

    learning_rate = [0.001, 0.0001] #, 0.0001, 0.00001
    epochs = 200 #50, 100, 150
    train_valid_loss_history = {}
    vaild_test_loss_history = {}


    for lr in range(len(learning_rate)): 
        FFN_model = FeedForwardNetwork(alphabets = alphabets , hidden_size = 32, languages = languages, max_length = max_length).to(device)
        train_loss_history = train_model(FFN_model, train_dataloader, device, epochs = 50, learning_rate = learning_rate[lr])
        accuarcy, min_loss, file_path, pickle_loss_and_model, loss_list = model_evaluate(FFN_model, valid_dataloader, device, learning_rate[lr])
        train_valid_loss_history[f'{lr}_model'] = [train_loss_history, loss_list]
        save_file(file_path, pickle_loss_and_model)

    accuarcy, min_loss, model, lr, valid_loss_list = valid(FFN_model, valid_dataloader, learning_rate, device)
    accuarcy, min_loss, file_path, pickle_loss_and_model, test_loss_list = model_evaluate(model, test_dataloader, device, lr)
    vaild_test_loss_history['valid_model'] = [valid_loss_list, test_loss_list]
    train_loss_history = train_model(model, train_dataloader, device, epochs = epochs, learning_rate = lr)
    accuarcy, min_loss, file_path, pickle_loss_and_model, test_loss_list = model_evaluate(model, test_dataloader, device, lr)

    vaild_test_loss_history['final_model'] = [train_loss_history, test_loss_list]



    plot_model(train_valid_loss_history, vaild_test_loss_history, epochs)


        
        
    
