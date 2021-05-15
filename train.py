import torch
import torch.nn as nn
import numpy as np
from package_testing.modules import utils

x = torch.randn(16, 10, 256, 256)
net = utils.ConvBlk(10, 30)

def train(num_epochs):
    for cur_epoch in range(num_epochs):
        print(f'Current Epoch: {cur_epoch}')