import torch
import torch.nn as nn 
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
from collections import defaultdict
from torch.utils.data import DataLoader, TensorDataset

from preprocessing import generate_dataset
from modeling import FeedForwardNetwork 
from train import train_model
from modify_ffn_dataset import ffn_dataset

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if __name__ == "__main__": 
    data, alphabets, max_length, languages  = generate_dataset()
    train_dataloader, valid_dataloader, test_dataloader = ffn_dataset(data, alphabets, max_length, languages)
    FFN_model = FeedForwardNetwork(alphabets = alphabets , hidden_size = 32, languages =languages, max_length = max_length).to(device)
    train_loss_history, valid_loss_history = train_model(FFN_model, train_dataloader, valid_dataloader, device, epochs = 100, learning_rate = 0.001)


