import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
file_path = r'C:\Users\Ross Home\Documents\GitHub\User-Behavior-eCommerce\data.csv'
df = pd.read_csv(file_path)

# Data Cleaning
df.dropna(subset = ['price', 'is_purchased'], inplace = True)  # Drop rows with missing critical values


### Exploartory Data Analysis

print(df.head(10))
print(df.info())
print("Dataset shape:", df.shape)
print("\nMissing values in each column:")
print(df.isnull().sum())
print("\nSummary statistics:")
print(df.describe())

# Display unique values for categorical columns 
print("\nUnique values in each categorical column:")

for column in df.select_dtypes(include = ['object']).columns:
    print(f"{column}: {df[column].nunique()}")


### Visualize the data

# Create a binned column for grouping price ranges
df['price_bin'] = pd.cut(df['price'], bins=np.arange(0, df['price'].max(), 100))

# Plot average purchase rate for each price bin
average_purchase_rate_by_price_bin = df.groupby('price_bin', observed = True)['is_purchased'].mean().reset_index()
plt.figure(figsize = (12, 6))
sns.barplot(x='price_bin', y='is_purchased', data=average_purchase_rate_by_price_bin, color='blue', alpha=0.7)
plt.xticks(rotation = 90)
plt.title('Average Purchase Rate by Price Bin')
plt.xlabel('Price Bin')
plt.ylabel('Average Purchase Rate')
plt.show()


# Price vs Activity Count
plt.figure("Price and Activity Count Scatterplot")
plt.scatter(df['price'], df['activity_count'])
plt.xlabel('Price')
plt.ylabel('Activity Count')
plt.title('Price vs. Activity Count')
plt.show()


# Correlation Heatmap
numeric_df = df.select_dtypes(include=[np.number])  # Select only numeric columns
correlation_matrix = numeric_df.corr()

plt.figure(figsize =( 10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square = True)
plt.title('Correlation Heatmap')
plt.show()


# Analyzing purchase rates by device type 
device_purchase_rates = df.groupby('subcategory')['is_purchased'].mean().reset_index()
plt.figure(figsize = (10, 6))
sns.barplot(x = 'subcategory', y = 'is_purchased', data = device_purchase_rates, palette='viridis')
plt.xticks(rotation = 90)
plt.title('Average Purchase Rate by Device Type')
plt.xlabel('Subcategory')
plt.ylabel('Average Purchase Rate')
plt.show()


# Convert timestamp column to datetime 
df['event_time'] = pd.to_datetime(df['event_time'])  # Convert to datetime
df.set_index('event_time', inplace = True)  # Set as index for resampling
daily_sales = df.resample('D')['is_purchased'].sum()  # Resample to daily sales

# Plot daily purchase trends
plt.figure(figsize=(12, 6))
daily_sales.plot()
plt.title('Daily Purchase Trends')
plt.xlabel('Date')
plt.ylabel('Number of Purchases')
plt.grid()
plt.show()


# Compare purchase rates across different price ranges
plt.figure(figsize=(12, 6))
sns.boxplot(x = 'price_bin', y = 'is_purchased', data = average_purchase_rate_by_price_bin)
plt.title('Purchase Rates Distribution by Price Bin')
plt.xlabel('Price Bin')
plt.ylabel('Purchase Rate')
plt.xticks(rotation = 90)
plt.show()


# Key Insights
print("Insights:")
print(f"Average purchase rate for highest price bin: {average_purchase_rate_by_price_bin['is_purchased'].max()}")
