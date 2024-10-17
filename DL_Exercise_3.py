# Use a FeedForward Neural Network to predict if a given Pokémon is **legendary** or not, based on *Pokémon features*.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

import torch
from torch import nn
import torch.optim as optim

