import torch
import torch.nn as nn 

class RNNManual(nn.Module):
    def __init__(self, input_dim, hidden_dim): 
        super(RNNManual, self).__init__()
        self.i2h = nn.Linear(input_dim, hidden_dim)
        self.h2h = nn.Linear(hidden_dim, hidden_dim)
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim

    def forward(self, x, hidden):
        return torch.tanh(self.i2h(x) + self.h2h(hidden))
    
    def init_hidden(self):
        return torch.zeros(self.hidden_dim)    
    
class RNNEncoder(nn.Module): 
    def __init__(self, eng_word2idx, eng_idx_sentence, max_length, hidden_dim = 32, embedding_dim = 200):
        super(RNNEncoder, self).__init__()
        self.cell = RNNManual(embedding_dim, hidden_dim)
        self.embedding = nn.Embedding(len(eng_idx_sentence)*max_length, embedding_dim)

    def forward(self, x, max_length): 
        hidden = self.cell.init_hidden()

        for i in range(max_length): 
            char = x[:, i]
            embedded = self.embedding(char).unsqueeze(1)
            hidden = self.cell(embedded, hidden)

        return hidden


     







        