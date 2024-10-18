import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F 
import random 
import matplotlib.pyplot as plt



def train_model(self, train_data, device, epochs, learning_rate): 
    criterion = F.nll_loss
    optimizer = optim.Adam(self.parameters(), lr = learning_rate)

    train_loss_history = []


    for epoch in  range(epochs):
        self.train()
        for x, y in train_data: 
            y_pred = self(x, device)
            loss = criterion(y_pred, y)

            loss.backward() 
            optimizer.step()
            optimizer.zero_grad() 

            mean_loss = torch.mean(loss).item() 

        if epoch % 10 == 0: 
            train_loss_history.append(mean_loss)
            print(f'Epoch : {epoch}, train_loss : {mean_loss}')
    
    # print("train_loss_history : ", train_loss_history)

    return train_loss_history

def plot_model(train_valid_loss_history, vaild_test_loss_history, epochs):
    for key, value in train_valid_loss_history: 
        plt.plot(epochs,value[0], label = f'{key}_train_loss')
        plt.plot(epochs,value[1], label = f'{key}_valid_loss')
    
    for key, value in vaild_test_loss_history: 
        plt.plot(epochs,value[0], label = f'{key}_valid_loss')
        plt.plot(epochs,value[0], label = f'{key}_test_loss')
    
    plt.show()

