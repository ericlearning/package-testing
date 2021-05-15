# package-testing
Experiments on packaging, VSCode, and Github Action

## Features
* Addition of two numbers
* Subtraction of two numbers
* Convolution Block

## Installation

Run the following command:
```python
pip install ufo
```

## Usage

```python
from ufo.utils import add, sub, ConvBlk

# add two numbers
add(3.4, 5.1)
add(-12, 7)

# subtract two numbers
sub(1.1, 9.1)
sub(-2, -6)

# create a convolutional block
net = utils.ConvBlk(10, 30)
```