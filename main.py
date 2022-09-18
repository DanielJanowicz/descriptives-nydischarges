## Importing packages
from dataclasses import dataclass
import pandas as pd
from tableone import Tableone, load_dataset
import researchpy as rp

## Creating dataframe for manipulation
data = pd.read_csv('data/NYSPARCS.csv')
data # 2343429 rows x 34 columns original size

# data1 = data.head(1000)
# data1

#### Cleaning up data ####
# data1.columns = data1.columns.str.replace('[^A-Za-z0-9]+', '_')
# data1.columns
# data1.to_csv('data/nysparcsdata.csv')

## Decreasing original dataset size for Pushing to GitHub
# data = data.head(100000)
# data.to_csv('data/NYSPARCS.csv')

data1 = pd.read_csv('data/nysparcsdata.csv')

## Obtaining information from researchpy 
rp.codebook(data1)
data1.columns
data1.dtypes

## Getting descriptives for variables in dataset
rp.summary_cat(data1[['Gender', 'Race', 'Type_of_Admission']])