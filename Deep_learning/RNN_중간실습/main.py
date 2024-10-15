import torch
import torch.nn as nn 
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
from collections import defaultdict
from torch.utils.data import DataLoader, TensorDataset

from preprocessing import generate_dataset



if __name__ == "__main__": 
    train_dataset, valid_dataset, test_dataset, alphabets, max_length, languages  = generate_dataset()



