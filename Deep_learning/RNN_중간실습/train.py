import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F 
import random 



def train_model(self, train_data, valid_data, device,  epochs = 100, learning_rate = 0.001,): 
    criterion = F.nll_loss
    optimizer = optim.Adam(self.parameters(), lr = learning_rate)

    step = 0 
    train_loss_history = []
    valid_loss_history = []

    train_log = {} 

    for epoch in  range(epochs):
        for x, y in train_data: 
            x.to(device)
            y.to(device)
            step += 1
            y_pred = self(x)
            loss = criterion(y_pred, y)

            loss.backward() 
            optimizer.step()
            optimizer.zero_grad() 

            mean_loss = torch.mean(loss).item() 

            if step % 10 == 0: 
                train_loss_history.append(mean_loss)
                print(f'Epoch : {epoch+1}, train_loss : {mean_loss}')

    return train_loss_history, valid_loss_history