import numpy as np


class ReLU:
  # Forward pass
  def forward(self, inputs):
    self.inputs = inputs
    self.output = np.maximum(0, inputs)

  # Backward pass
  def backward(self, dvalues):
    self.dinputs = dvalues.copy()
    # Zero gradient where input values were negative
    self.dinputs[self.inputs <= 0] = 0