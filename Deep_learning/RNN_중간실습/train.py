import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F 
import random 



def train_model(self, train_data, valid_data, device, epochs = 100, learning_rate = 0.001): 
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
    
    print("train_loss_history : ", train_loss_history)

    return train_loss_history
