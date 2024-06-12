import torch
import torch.nn as nn
from torch.nn import functional as F

torch.manual_seed(777)

# Hyperparameters
context_length = 8 # How much are we feeding the transformer at the same time, also known as block size. In this case 8 numbers
batch_size = 4 # Independent sequences processed in parallel
device = 'cuda' if torch.cuda.is_available() else 'cpu'
learning_rate = 3e-4
max_iters = 10000

# Open file and create vocab
text = open('data/Friends_Transcript.txt', 'r').read()
vocab = sorted(list(set(text)))
vocab_size = len(vocab)

# Encoder / Decoder
stoi = {ch:i for i,ch in enumerate(vocab)}
itos = {i:ch for i,ch in enumerate(vocab)}
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])


# Train-Test split
data = torch.tensor(encode(text), dtype = torch.long)
train_n = int(len(data)*0.95)
train_ds = data[:train_n]
test_ds = data[train_n:]


def get_batch(split):
    data = train_ds if split == 'train' else test_ds
    ix = torch.randint(len(data) - context_length, (batch_size,))
    x = torch.stack([data[i:i+context_length] for i in ix])
    y = torch.stack([data[i+1:i+context_length+1] for i in ix])
    x, y = x.to(device), y.to(device)
    return x, y