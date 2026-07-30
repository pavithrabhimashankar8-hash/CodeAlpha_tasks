import pandas as pd

print("=" * 60)
print("      CODEALPHA DATA ANALYTICS - TASK 2")
print("       EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# Read CSV File
data = pd.read_csv("scraped_data.csv")

print("\nDataset Loaded Successfully")

# Display first 10 rows
print("\nFirst 10 Records")
print(data.head(10))

# Dataset Shape
print("\nDataset Shape")
print(data.shape)

# Column Names
print("\nColumn Names")
print(data.columns)

# Dataset Information
print("\nDataset Information")
print(data.info())

# Missing Values
print("\nMissing Values")
print(data.isnull().sum())

# Statistical Summary
print("\nStatistical Summary")
print(data.describe(include='all'))

# Rating Count
print("\nBook Ratings Count")
print(data["Rating"].value_counts())

print("\nEDA Completed Successfully")
print("=" * 60)