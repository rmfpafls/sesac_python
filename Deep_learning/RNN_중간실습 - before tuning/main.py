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
from modeling import FeedForwardNetwork, RNN
from train import train_model
from modify_ffn_dataset import ffn_dataset
from evaluate import model_evaluate, save_file
from valid import valid
from debugger import debug_shell

device = torch.device("cpu")#  if torch.cuda.is_available() )

def plot(train_loss_history, vaild_loss_history): 
    plot_x = []
    plot_y = []

    for loss_histrory in train_loss_history: 
        plot_x = []
        plot_y = []
        for key, value in loss_histrory.items():
                plot_x.append(key[0])
                plot_y.append(value)
                plot_learning_rate = key[1]
                print(key, value)
        plt.plot(plot_x, plot_y, label = f'{plot_learning_rate}_train_loss')


    for loss_histrory in vaild_loss_history: 
        plot_x = []
        plot_y = []
        for key, value in loss_histrory.items():
                plot_x.append(key[0])
                plot_y.append(value)
                plot_learning_rate = key[1]
                print(key, value)
        plt.plot(plot_x, plot_y, label = f'{plot_learning_rate}_valid_loss')

    plt.legend()
    plt.show()


if __name__ == "__main__": 
    x,y, alphabets, max_length, languages, batch_size  = generate_dataset()
    train_dataloader, valid_dataloader, test_dataloader = ffn_dataset(x,y, batch_size)

    learning_rate = [0.001, 0.0001] #, 0.0001, 0.00001
    epochs = 100 #50, 100, 150
    train_loss_history = []
    vaild_loss_history = []
    file_path = 'loss_history.pkl'

    for lr in range(len(learning_rate)): 
        model = FeedForwardNetwork(alphabets = alphabets , hidden_size = 32, languages = languages, max_length = max_length).to(device)
        # model = RNN(alphabets, hidden_size = 32, languages = languages, max_length = max_length)
        train_loss_history_dict, valid_loss_history, pickle_loss_and_model = train_model(model, train_dataloader, valid_dataloader, device, epochs = epochs, learning_rate = learning_rate[lr])
        train_loss_history.append(train_loss_history_dict)
        vaild_loss_history.append(valid_loss_history)

        save_file(file_path, pickle_loss_and_model)

    accuarcy, min_loss, model, lr, loss_list = valid(model, valid_dataloader, learning_rate, device)   
    accuarcy, min_loss, pickle_loss_and_model, test_loss_list = model_evaluate(model, test_dataloader, device, lr)
    
    print("Test accuaruacy : ", accuarcy)
    print("Test_min_loss :", min_loss)

    plot(train_loss_history, vaild_loss_history)


    
        
        
    
