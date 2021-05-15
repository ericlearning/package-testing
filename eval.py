import torch
from package_testing.modules import utils

def eval():
    print("Evaluation in progress ...")
    x = torch.randn(16, 10, 256, 256)
    net = utils.ConvBlk(10, 30)
    return net(x)