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
from train import train_model
from modify_ffn_dataset import ffn_dataset
from evaluate import model_evaluate

device = torch.device("cpu")#  if torch.cuda.is_available() )

if __name__ == "__main__": 
    x,y, alphabets, max_length, languages, batch_size  = generate_dataset()
    train_dataloader, valid_dataloader, test_dataloader = ffn_dataset(x,y, batch_size)

    learning_rate = [0.001] #, 0.0001, 0.00001
    epoch_list = [100, 150] #50, 100, 150


    for lr in learning_rate: 
        for epoch in epoch_list: 
            FFN_model = FeedForwardNetwork(alphabets = alphabets , hidden_size = 32, languages = languages, max_length = max_length).to(device)
            train_loss_history = train_model(FFN_model, train_dataloader, valid_dataloader, device, epochs = epoch, learning_rate = lr)
            accuarcy, min_loss = model_evaluate(FFN_model, valid_dataloader, device, epoch, lr)

    # accuarcy, min_loss = model_evaluate()
    e = pickle.load(open('loss_history.pkl', 'rb'))
    print("e :", e)
