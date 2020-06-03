import numpy as np
import pandas as pd

from hmmlearn import hmm

temporal_dataset = pd.read_csv("./../../ftd/FTDD/temporal_activity.csv",header=None)

temporal_sequence = pd.DataFrame()

#print(temporal_dataset[0][1])


for index, row in temporal_dataset.iterrows():
    if row[0] not in temporal_sequence.index:
        temporal_sequence[row[0]]=[row[2]]
    else:
        temporal_sequence[row[0]].append(row[2])

    if index==500:
        break
    #print(row[0])

print(temporal_sequence[322067])

