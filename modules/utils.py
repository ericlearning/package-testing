import torch
import torch.nn as nn
import numpy as np

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

class ConvBlk(nn.Module):
    def __init__(self, ic, oc):
        super().__self__()
        self.m = nn.Sequential(
            nn.Conv2d(ic, oc, 3, 1, 1),
            nn.BatchNorm2d(oc),
            nn.ReLU())

    def forward(self, x):
        return self.m(x)