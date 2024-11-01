import torch 
import torch.nn as nn 
import torch.optim as optim
import matplotlib.pyplot as plt
from time import time 
from typing import List
import math
import pickle
import os 
import numpy as np
from torch.utils.data import DataLoader

from conv2d_mine import CNN 
from conv2d_torch import SimpleCNN
from data_handler import train_data, train_loader, small_train_loader, valid_loader
from debug_shell import debug_shell

def validate_model(
    model : nn.Module,
    dataset : torch.utils.data.DataLoader, 
    criterion : nn.Module,
    save_loss : float = math.inf,
    state_dict : dict = {},
    ) -> List[float]:

    model.eval() 
    valid_loss_history = []
    correct : int = 0,
    total : int = 0
    
    with torch.no_grad(): 
        for x, y in dataset: 
            valid_begin = time()
            y_pred = model(x)
            valid_end = time()
            y_pred = torch.argmax(y_pred, dim = -1)
            loss = criterion(y_pred, y)
            loss_mean = torch.mean(loss).item()

            valid_loss_history.append(loss_mean)
            valid_count_time = round(valid_begin - valid_end)

            correct += torch.sum(y_pred == y)
            total +=  y.size(0)
            valid_accuracy = (correct / total)

            if save_loss > loss_mean: 
                save_loss = loss_mean
                state_dict[loss_mean] = model.state_dict()        

        return valid_count_time, valid_loss_history, valid_accuracy, state_dict, loss_mean


def train(
    model: nn.Module, 
    train_loader: torch.utils.data.DataLoader, 
    valid_loader: torch.utils.data.DataLoader, 
    criterion: nn.Module, 
    optimizer: torch.optim, 
    epochs: int = 10, 
    lr: float = 0.001, 
) -> List[float]:
    
    model.train()
    train_loss_history = []
    optimizer = optimizer(model.parameters(), lr = lr)

    for epoch in range(1, 1 + epochs):
        epoch_loss = 0
        no_batches = 0
        begin = time()
        
        for batch_x, batch_y in train_loader:
            out = model(batch_x) 
            batch_y = batch_y.long()
            loss = criterion(out, batch_y)

            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            
            epoch_loss += loss.item() 
            no_batches += 1 
        end = time() 
        train_loss_history.append(epoch_loss / no_batches)
        valid_count_time, valid_loss_history, valid_accuracy, state_dict, loss_mean = validate_model(model, valid_loader, 
                                                                                                      )
        print(f'[epoch {epoch}/epochs] train loss : {round(epoch_loss / no_batches, 4)}, {round(end - begin, 4)} sec passed.')
        print(f'[epoch {epoch}/epochs] valid loss : {round(loss_mean, 4)}, valid_accuracy : {valid_accuracy} ,  {round(valid_count_time, 4)} sec passed.')

    return train_loss_history, valid_loss_history

def plot_loss_history(loss_history):
    """
    Plots the training and validation loss history.

    Parameters:
    - loss_history (dict): A dictionary containing 'train' and 'val' loss lists.

    Example usage:
    loss_history = {'train': [0.9, 0.7, 0.5], 'val': [1.0, 0.8, 0.6]}
    plot_loss_history(loss_history)
    """
    plt.figure(figsize=(10, 6))
    plt.plot(loss_history, label='Training Loss')
    
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss History')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    model = SimpleCNN()
    train_loss_history, validate_loss_history = train(
        model, 
        train_loader, 
        valid_loader,
        criterion = nn.CrossEntropyLoss(), 
        optimizer = optim.Adam, 
        epochs = 10, 
        lr = 0.001, 
    )




    plot_loss_history(train_loss_history)