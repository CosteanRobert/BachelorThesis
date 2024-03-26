import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import torch
from torch.utils.data import DataLoader, TensorDataset

def load_and_process_data(filepath, seq_length=5):
    # Load the data
    data = pd.read_csv(filepath)

    # Select relevant features
    features = data[['Close', 'Volume', 'MACD', 'Signal_Line', 'RSI']].values
    targets = data[['Close']].values[1:]

    # Normalize the features
    scaler = MinMaxScaler(feature_range=(-1, 1))
    features_normalized = scaler.fit_transform(features)
    targets_normalized = scaler.fit_transform(targets)

    # Create sequences
    X, y = create_sequences(features_normalized, targets_normalized, seq_length)

    # Splitting the data into training and test sets
    train_size = int(len(X) * 0.8)
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Converting to PyTorch tensors
    X_train_tensor, y_train_tensor = torch.FloatTensor(X_train), torch.FloatTensor(y_train)
    X_test_tensor, y_test_tensor = torch.FloatTensor(X_test), torch.FloatTensor(y_test)

    # Creating DataLoader
    train_data = TensorDataset(X_train_tensor, y_train_tensor)
    train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

    return train_loader, X_test_tensor, y_test_tensor

def create_sequences(input_data, target_data, sequence_length):
    xs, ys = [], []
    for i in range(len(input_data)-sequence_length):
        x = input_data[i:(i+sequence_length)]
        y = target_data[i+sequence_length]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)
