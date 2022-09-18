## Importing packages
from dataclasses import dataclass
import pandas as pd
from tableone import Tableone, load_dataset
import researchpy as rp

## Creating dataframe for manipulation
data = pd.read_csv('data/NYSPARCS.csv')
data # 2343429 rows x 34 columns

data1 = data.head(50000)
data1

data1.to_csv('data/nysparcsdata.csv')

## Decreasing original dataset size for Pushing to GitHub
data = data.head(100000)
data.to_csv('data/NYSPARCS.csv')