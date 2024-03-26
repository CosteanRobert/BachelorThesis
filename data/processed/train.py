import torch
import torch.nn as nn
import torch.optim as optim
from data.processed.data_preprocessing import load_and_process_data
from data.processed.model import SimpleLSTM

# Load data
train_loader, X_test, y_test = load_and_process_data('AAPL_stock_data_with_indicators.csv', 5)

# Initialize model, loss function, and optimizer
model = SimpleLSTM(input_size=5, hidden_layer_size=100, output_size=1)
loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training loop
epochs = 10
for epoch in range(epochs):
    for seq, labels in train_loader:
        optimizer.zero_grad()
        model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size),
                            torch.zeros(1, 1, model.hidden_layer_size))
        y_pred = model(seq)
        single_loss = loss_function(y_pred, labels)
        single_loss.backward()
        optimizer.step()
    print(f'Epoch {epoch} loss: {single_loss.item()}')

# Add evaluation code here if needed
