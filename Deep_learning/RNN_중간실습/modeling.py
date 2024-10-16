import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F 
import random 



class FeedForwardNetwork(nn.Module): 
    def __init__(self, alphabets, hidden_size, languages, max_length): 
        super(FeedForwardNetwork, self).__init__()
        self.layer1 = nn.Linear(len(alphabets) * max_length, hidden_size) #384 
        self.layer2 = nn.Linear(hidden_size, len(languages)) #32 18
        self.alphabets = alphabets
        self.max_length = max_length

    def forward(self, x):
        output = self.layer1(x).to(device)
        output = F.relu(output).to(device)
        output = self.layer2(output).to(device)
        output = F.log_softmax(output, dim = 1).to(device)
        return output
