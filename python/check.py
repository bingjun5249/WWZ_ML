import torch
import torch.nn as nn
import torch.nn.functional as F

neurons = 4096

class Model(nn.Module):

	def __init__(self):
		super(Model, self).__init__()
		self.flatten = nn.Flatten()
		self.fc = nn.Sequential(

			# 1st layer
			nn.Linear(8, neurons),
			nn.ReLU(),
			nn.BatchNorm1d(neurons),
			nn.Dropout(0.5),
			
			# 2nd layer
            		nn.Linear(neurons, neurons),
			nn.ReLU(),
			nn.BatchNorm1d(neurons),
			nn.Dropout(0.5),
			
			# 3rd layer
         		nn.Linear(neurons, neurons),
			nn.ReLU(),
			nn.BatchNorm1d(neurons),
			nn.Dropout(0.5),

        		# 4th layer
			nn.Linear(neurons, neurons),
			nn.ReLU(),
			nn.BatchNorm1d(neurons),
			nn.Dropout(0.5),

          		# 5th layer
	       		nn.Linear(neurons, neurons),
			nn.ReLU(),
			nn.BatchNorm1d(neurons),
			nn.Dropout(0.5),

	       		nn.Linear(neurons, neurons),
			nn.ReLU(),
			nn.BatchNorm1d(neurons),
			nn.Dropout(0.5),

			# 7th layer
			nn.Linear(neurons, 64),
			nn.ReLU(),
			nn.BatchNorm1d(64),

			# 8th layer
            		nn.Linear(64, 1),
			nn.Sigmoid(),
		)


	def forward(self, x):
		y_pred = self.fc(x)
		return y_pred


device = "cuda" if torch.cuda.is_available() else "cpu"

model = torch.load("../storage/run_files/total/trial10/total_weightFile.pth", map_location=device)
print(model)
