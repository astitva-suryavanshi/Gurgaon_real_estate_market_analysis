import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import csv file to dataframe
df = pd.read_csv('data.csv')
# print(df.head())
# print(df.columns)
# print(df.info())
# -------------------------------------------------------------------------------------------------
# data cleaning
# cleaning all the columns 
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
# print(df.columns)
# deleating all dublicates values
df = df.drop_duplicates()
# -------------------------------------------------------------------------------------------------
# numeric column cleaning
df['price'] = df['price'].astype(str).str.replace(",", "").astype(float)
df['area'] = df['area'].astype(str).str.replace(",", "").astype(int)
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(",", "").astype(int)
# print(df['price'])
# print(df['rate_per_sqft'])
# -------------------------------------------------------------------------------------------------
# Categorical columns cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera':True, 'not approved by rera': False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()

df = df.drop_duplicates()

# print(df)
# print(df.info())
# -------------------------------------------------------------------------------------------------
# Question 1: Which is the costliest flat?
print(df.loc[df["price"].idxmax()])
'''
# price                                1226300000.0
# status                              ready to move
# area                                        16500
# rate_per_sqft                               74323
# property_type    6 BHK Apartment in DLF Camellias
# locality                                Sector 42
# builder_name                    Provident Capital
# rera_approval                               False
# bhk_count                                       6
# society                             DLF Camellias
# company_name                                  DLF
# flat_type                               apartment
'''
# -------------------------------------------------------------------------------------------------
#QUESTION 2 - Which locality has the highest average price?
highest_avg_price_locality = df.groupby('locality')['price'] .mean().idxmax()
print(f'highest average price locality is : {highest_avg_price_locality}')
# -------------------------------------------------------------------------------------------------
#QUESTION 3 - Which locality has the highest rate per square foot?
highest_rate_per_sq_foot = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"locality with highest rate per sqft is : {highest_rate_per_sq_foot}")
# -------------------------------------------------------------------------------------------------
#QUESTION 4 - Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()

if ready_to_move_avg_price > under_construction_avg_price:
    print("ready to move property cost more on average than under construction property")
else:
    print("under construction properties cost more than ready to move property")
# -------------------------------------------------------------------------------------------------
# QUESTION 5 - Do RERA-approved properties command a price premium?
rera_aprooved_avg_price = df[df['rera_approval'] == True]['price']
# -------------------------------------------------------------------------------------------------
# QUESTION 6 - How does area (sqft) impact property price?
sns.scatterplot(data=df, x= 'area', y='price')
plt.show()
# -------------------------------------------------------------------------------------------------
# QUESTION 7 - Which BHK configuration is the most expensive on average?
most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"most ecpensive BHK configuration on average is : {most_expensive_bhk} bhk")
# -------------------------------------------------------------------------------------------------
# QUESTION 8 - Which property type (Apartment, Floor, Plot) is the costliest?
costliest_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"costliest property type is : {costliest_property_type}")
# -------------------------------------------------------------------------------------------------
# QUESTION 9 - Do certain builders or companies consistently price higher?
print(df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5))
# -------------------------------------------------------------------------------------------------
# QUESTION 10 - Are larger homes always more expensive per square foot?
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.show()