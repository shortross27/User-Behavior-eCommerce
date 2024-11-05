import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
file_path = r'C:\Users\Ross Home\Documents\GitHub\User-Behavior-eCommerce\data.csv'
df = pd.read_csv(file_path)



# Exploartory Data Analysis

# Display the first few rows of the dataset
print(df.head(10))

# Display basic information about the dataset
print(df.info())

# Display the shape of the dataset (number of rows and columns)
print("Dataset shape:", df.shape)

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Display summary statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())

# Display unique values for categorical columns (if applicable)
print("\nUnique values in each categorical column:")

for column in df.select_dtypes(include = ['object']).columns:
    print(f"{column}: {df[column].nunique()}")


# Visualize the data

# Create a binned column for grouping price ranges
df['price_bin'] = pd.cut(df['price'], bins=np.arange(0, df['price'].max(), 100))

# Plot average purchase rate for each price bin
avg_purchase_per_bin = df.groupby('price_bin')['is_purchased'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='price_bin', y='is_purchased', data=avg_purchase_per_bin, color='blue', alpha=0.7)
plt.xticks(rotation=90)
plt.title('Average Purchase Rate by Price Bin')
plt.xlabel('Price Bin')
plt.ylabel('Average Purchase Rate')
plt.show()

#Plot with Matplotlib
plt.figure("Price and Activity Count Scatterplot")
plt.scatter(df['price'], df['activity_count'])
plt.xlabel('Price')
plt.ylabel('Activity Count')
plt.title('Price vs. Activity Count')
plt.show()

