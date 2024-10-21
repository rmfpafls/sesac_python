import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F 
import random 
import matplotlib.pyplot as plt

from evaluate import model_evaluate

def train_model(self, train_data, valid_dataloader, device, epochs, learning_rate): 
    criterion = F.nll_loss
    optimizer = optim.Adam(self.parameters(), lr = learning_rate)

    train_loss_history = {}
    valid_loss_history = {} 

    for epoch in  range(epochs):
        self.train()
        epoch_loss = 0
        batch_count = 0

        for x, y in train_data: 
            # y_pred = self(x, device) # ffn
            y_pred = self(x, device, hidden = 32)
            loss = criterion(y_pred, y)

            loss.backward() 
            optimizer.step()
            optimizer.zero_grad() 
            epoch_loss += loss.item()
            batch_count += 1

        train_mean_loss = epoch_loss / batch_count
        train_loss_history[(epoch, learning_rate)] = train_mean_loss

        valid_loss, valid_accuracy, pickle_loss_and_model = validate_model(self, valid_dataloader, device, learning_rate)
        valid_mean_loss = valid_loss
        valid_loss_history[(epoch, learning_rate)] = valid_mean_loss

        if epoch % 10 == 0: 
            print(f'Epoch : {epoch}, train_loss : {train_mean_loss}')
            print(f'Epoch : {epoch}, valid_loss : {valid_mean_loss}, valid_accuracy : {valid_accuracy}')

    return train_loss_history, valid_loss_history, pickle_loss_and_model

def validate_model(self, valid_dataloader, device, learning_rate): 
    accuarcy, min_loss, pickle_loss_and_model, loss_list =  model_evaluate(self, valid_dataloader, device, learning_rate)
    valid_accuracy = accuarcy
    valid_loss = min_loss
    return valid_loss, valid_accuracy, pickle_loss_and_model


# def plot_model(train_valid_loss_history, vaild_test_loss_history, epochs):
#     for key, value in train_valid_loss_history.items(): 
#         plt.plot(epochs, value[0], label = f'{key}_train_loss')
#         plt.plot(epochs, value[1], label = f'{key}_valid_loss')
    
#     for key, value in vaild_test_loss_history.items(): 
#         plt.plot(epochs, value[0], label = f'{key}_valid_loss')
#         plt.plot(epochs, value[0], label = f'{key}_test_loss')
    
#     plt.show()

