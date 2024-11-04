import pandas as pd
import matplotlib as plt
import seaborn as sns

# Load the dataset
file_path = r'C:\Users\Ross Home\Documents\GitHub\User-Behavior-eCommerce\data.csv'
df = pd.read_csv(file_path)



# Exploartory Data Analysis

# Display the first few rows of the dataset
print(df.head())

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

for column in df.select_dtypes(include=['object']).columns:
    print(f"{column}: {df[column].nunique()}")



# Visualize the data

purchase_rates = df.groupby('price')['is_purchased'].mean().reset_index()

# Plotting
plt.figure(figsize=(10, 6))
sns.lineplot(data=purchase_rates, x='price', y='is_purchased')
plt.title('Purchase Rates by Price')
plt.xlabel('Price')
plt.ylabel('Purchase Rate')
plt.grid()
plt.show()
