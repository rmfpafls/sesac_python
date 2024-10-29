import torch 
import torch.nn as nn 
import torch.nn.functional as F
import torch.optim as optim

class BatchNormalization(nn.Module):
    def __init__(self, hidden_dim, batch_dim = 0 ):
        super(BatchNormalization, self).__init__()
        self.gamma = nn.Parameter(torch.ones(hidden_dim))
        # nn.Parameter : 주로 모델의 학습 가능한 매개변수를 정의하기 위해 사용된다. 
        self.beta = nn.Parameter(torch.zeros(hidden_dim))
        self.eps = 1e-6
        self.batch_dim = 0
    
    def forward(self, x):
        mean = x.mean(dim = self.batch_dim) 
        std = x.var(dim = self.batch_dim) 
        x_hat = (x - mean) / torch.sqrt(std + self.eps)

        return self.gamma * x_hat + self.beta
