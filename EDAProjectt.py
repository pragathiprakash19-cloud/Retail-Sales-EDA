# =========================================
# RETAIL SALES DATA ANALYSIS (EDA PROJECT)
# =========================================

# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# =========================================
# 2. Data Loading
# =========================================

# Load dataset
df = pd.read_csv("retail_sales_dataset.csv")

print("First 5 rows")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nColumns:")
print(df.columns)

# =========================================
# 3. Data Cleaning
# =========================================

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values and duplicates
df = df.dropna()
df = df.drop_duplicates()

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Create month column
df['Month'] = df['Date'].dt.month

print("\nData after cleaning:", df.shape)

# =========================================
# 4. Descriptive Statistics
# =========================================

print("\nStatistical Summary")
print(df.describe())

print("\nMean Sales:", df['Sales'].mean())
print("Median Sales:", df['Sales'].median())
print("Mode Sales:", df['Sales'].mode()[0])
print("Standard Deviation:", df['Sales'].std())

# =========================================
# 5. Time Series Analysis
# =========================================

daily_sales = df.groupby('Date')['Sales'].sum()

plt.figure(figsize=(10,5))
daily_sales.plot()
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

# Monthly sales trend
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(8,5))
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# =========================================
# 6. Customer Analysis
# =========================================

gender_sales = df.groupby('Gender')['Sales'].sum()

plt.figure(figsize=(6,4))
gender_sales.plot(kind='bar')
plt.title("Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Sales")
plt.show()

# =========================================
# 7. Product Analysis
# =========================================

category_sales = df.groupby('Product Category')['Sales'].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind='bar')
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# =========================================
# 8. Visualization
# =========================================

# Sales distribution
plt.figure(figsize=(8,5))
plt.hist(df['Sales'], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Correlation heatmap
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# =========================================
# 9. Insights / Recommendations
# =========================================

print("\nBusiness Insights:")
print("1. Identify high selling product categories.")
print("2. Improve marketing during low sales months.")
print("3. Focus on high spending customer segments.")
print("4. Increase promotion for popular products.")