import torch
import torch.nn as nn 

class SimpleCNN(nn.Module):
    def __init__(
        self, 
        num_classes: int = 10
    ): 
        super(SimpleCNN, self).__init__() 
        self.conv1: nn.Conv2d = nn.Conv2d(
            in_channels = 3, 
            out_channels = 16, 
            kernel_size = 3, 
            padding = 1, 
        )
        self.relu: nn.ReLU = nn.ReLU() 
        self.pool: nn.MaxPool2d = nn.MaxPool2d(kernel_size = 2, stride = 2)
        self.conv2: nn.Conv2d = nn.Conv2d(
            in_channels = 16, 
            out_channels = 32, 
            kernel_size = 3, 
            padding = 1
        )
        self.fc: nn.Linear = nn.Linear(32 * 8 * 8, num_classes)

    def forward(self, x: torch.tensor) -> torch.tensor:
        # x: (batch_size, 3, 32, 32)
        batch_size = x.size(0) 
        x = self.conv1(x) # (batch_size, 16, 32, 32)
        x = self.relu(x) 
        x = self.pool(x) # (batch_size, 16, 16, 16) 
        x = self.conv2(x) # (batch_size, 32, 16, 16) 
        x = self.relu(x) 
        x = self.pool(x) # (batch_size, 32, 8, 8) 
        x = x.view(batch_size, -1)  # (batch_size, 32 * 8 * 8)
        x = self.fc(x) 
        return x 