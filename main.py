## Importing packages
from dataclasses import dataclass
import pandas as pd
from tableone import TableOne, load_dataset
import researchpy as rp


##### Creating dataframe for manipulation #####
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
################################################


## Obtaining information from researchpy 
rp.codebook(data1)
data1.columns
data1.dtypes

## Getting descriptives for variables in dataset
rp.summary_cat(data1[['Gender', 'Race', 'Type_of_Admission']])

data1_gender = data1['Gender'].value_counts() 
data1_race = data1['Race'].value_counts()
data1_admission_type = data1['Type_of_Admission'].value_counts()
data1_payment_type = data1['Payment_Typology_1'].value_counts()
data1_description = data1['APR_MDC_Description'].value_counts()


### Grouping of information in the dataset ###
df1_columns = ['Gender', 'Race', 'Type_of_Admission']
df1_categorical = ['Type_of_Admission', 'Race']
df1_groupby = ['Gender']
df1_table = TableOne(data1, columns=df1_columns, 
    categorical=df1_categorical, groupby=df1_groupby, pval=False)

print(df1_table.tabulate(tablefmt = "fancy_grid"))
# Grid can help explain the percentage of the types of admission and their race based on gender

### Providing values within the dataset ###
print(data1_gender)
print(data1_race)
print(data1_admission_type)
print(data1_payment_type)
print(data1_description)

##### Calculating mean age #####
data1['Age_Group'].unique() # Obtaining unique data names

## Assigning variables
df_count = data1['Age_Group'].count()
df_really_old = 0 # 70 or older
df_semi_old = 0 # 50-69
df_mid_old = 0 # 30-49
df_young = 0 # 18-29
df_really_young = 0 # 0-17

age = data1['Age_Group']

def age_counter(age):
    if age == '70 or Older':
        global df_really_old
        df_really_old += 1
        return df_really_old
    elif age == '50-69':
        global df_semi_old
        df_semi_old += 1
        return df_semi_old
    elif age == '30-49':
        global df_mid_old
        df_mid_old += 1
        return df_mid_old
    elif age == '18-29':
        global df_young
        df_young += 1
        return df_young
    elif age == '0-17':
        global df_really_young
        df_really_young + 1
        return df_really_young
        
## Could not get this to work ^ 


