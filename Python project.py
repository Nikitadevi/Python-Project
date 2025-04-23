
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel File
df=pd.read_csv("project.csv")

# 1. DATA CLEANING
print("Initial Shape:", df.shape)

# Check for missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Drop rows with missing pollutant data
df_clean = df.dropna(subset=['pollutant_min', 'pollutant_max', 'pollutant_avg'])

# Check data types and info
print("\nCleaned Data Info:")
print(df_clean.info())

# 2. BASIC STATISTICS
print("\nSummary Statistics:")
print(df_clean.describe(include='all'))

# 3. POLLUTANT DISTRIBUTION
plt.figure(figsize=(10, 6))
sns.countplot(data=df_clean, y='pollutant_id', order=df_clean['pollutant_id'].value_counts().index) # Use a red color palette
plt.title('Pollutant Count Distribution')
plt.xlabel('Count')
plt.ylabel('Pollutant ID')
plt.tight_layout()
plt.show()

# 7. STATES WITH HIGHEST AVERAGE POLLUTION
top_states = df_clean.groupby('state')['pollutant_avg'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6), facecolor='black')
sns.set_style("darkgrid")
plt.title("Top 10 Polluted States (Avg Level)", color='white')
plt.xlabel("Average Pollution", color='white')
plt.ylabel("State", color='white')
plt.xticks(color='white')
plt.yticks(color='white')
plt.tight_layout()
plt.show()

# 8. INSIGHT SUMMARY
print("\n--- INSIGHTS ---")
print(f"Most common pollutant: {df_clean['pollutant_id'].value_counts().idxmax()}")
print(f"Total stations: {df_clean['station'].nunique()}")
print(f"Cities monitored: {df_clean['city'].nunique()}")
print(f"States monitored: {df_clean['state'].nunique()}")
print(f"Highest average pollution level: {df_clean['pollutant_avg'].max()}")




import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# 4. CORRELATION BETWEEN POLLUTANT VALUES
corr = df_clean[['pollutant_min', 'pollutant_max', 'pollutant_avg']].corr()

plt.figure(figsize=(6, 4), facecolor='black') # Set figure facecolor to black
plt.style.use('dark_background') # Use dark background style

sns.heatmap(corr, annot=True, cmap='Reds', fmt='.2f', linewidths=.5, linecolor='red') # Use 'Reds' colormap
plt.title('Correlation between Pollutant Values', color='white') # Set title color
plt.xticks(color='white') # Set x-axis tick color
plt.yticks(color='white') # Set y-axis tick color
plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 6), facecolor='black')
plt.style.use('dark_background')

# Calculate avg_pollutant before using it
avg_pollutant = df_clean.groupby('pollutant_id')['pollutant_avg'].mean().sort_values(ascending=False)

sns.barplot(x=avg_pollutant.values, y=avg_pollutant.index, palette='Reds_r') # Use reversed Reds palette for dark theme
plt.title("Average Pollution Level by Pollutant", color='white')
plt.xlabel("Average Value", color='white')
plt.ylabel("Pollutant", color='white')
plt.xticks(color='white')
plt.yticks(color='white')
plt.tight_layout()
plt.show()



# 6. TOP 10 POLLUTED CITIES (by average pollutant level)
top_cities = df_clean.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6), facecolor='black')
plt.style.use('dark_background')

sns.barplot(x=top_cities.values, y=top_cities.index, palette='Reds_r') # Use reversed Reds palette
plt.title("Top 10 Polluted Cities (Avg Level)", color='white', fontsize=16)
plt.xlabel("Average Pollution", color='white')
plt.ylabel("City", color='white')
plt.xticks(color='white')
plt.yticks(color='white')
plt.tight_layout()
plt.show()




import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# 8. INSIGHT SUMMARY (No changes needed here)
print("\n--- INSIGHTS ---")
print(f"Most common pollutant: {df_clean['pollutant_id'].value_counts().idxmax()}")
print(f"Total stations: {df_clean['station'].nunique()}")
print(f"Cities monitored: {df_clean['city'].nunique()}")
print(f"States monitored: {df_clean['state'].nunique()}")
print(f"Highest average pollution level: {df_clean['pollutant_avg'].max()}")





# Example of a boxplot with dark red theme
plt.figure(figsize=(10, 6), facecolor='black')
plt.style.use('dark_background')

sns.boxplot(x='pollutant_id', y='pollutant_avg', data=df_clean, palette='Reds', showfliers=False) #Removed outliers for clarity
plt.title("Distribution of Average Pollutant Levels by Pollutant ID", color='white', fontsize=16)
plt.xlabel("Pollutant ID", color='white')
plt.ylabel("Average Pollutant Level", color='white')
plt.xticks(color='white')
plt.yticks(color='white')
plt.tight_layout()
plt.show()




# 6. TOP 10 POLLUTED CITIES (by average pollutant level) - PIE CHART
top_cities = df_clean.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6), facecolor='black')
plt.style.use('dark_background')

# Create the pie chart
plt.pie(top_cities.values, labels=top_cities.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Reds(range(10)))  # Use Reds colormap

plt.title("Top 10 Polluted Cities (Avg Level)", color='white', fontsize=16)
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()




# Pair Plot
plt.figure(figsize=(10, 8), facecolor='black')
plt.style.use('dark_background')

sns.pairplot(df_clean[['pollutant_min', 'pollutant_max', 'pollutant_avg']],
             plot_kws={'color': 'red', 'alpha': 0.5}, diag_kws={'color':'red'}) # set color for points and diag
plt.suptitle("Pair Plot of Pollutant Values", color='white', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96]) # adjust the rect to make space for suptitle
plt.show()

