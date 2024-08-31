import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the data (assuming the CSV file is in the same directory)
netflix_data = pd.read_csv('Netflix_shows_movies.csv')

# Get information about the dataset
print(netflix_data.info())

# Check for missing values
print(netflix_data.isnull().sum())

# Handle missing values (e.g., dropping or imputing)
netflix_data_cleaned = netflix_data.dropna()  # Or use imputation methods if needed

# Save the cleaned dataset if necessary
netflix_data_cleaned.to_csv('C:\\Users\\Admin\\Desktop\\Module4Work\\Netflix_shows_movies_cleaned.csv', index=False)
# Generate data descriptions
print(netflix_data_cleaned.describe())
# Visualization 1: Most Watched Genres
plt.figure(figsize=(12, 6))
sns.countplot(data=netflix_data_cleaned, x='listed_in', order=netflix_data_cleaned['listed_in'].value_counts().index)
plt.title('Most Watched Genres')
plt.xticks(rotation=90)
plt.xlabel('Genre')
plt.ylabel('Count')
plt.savefig('C:\\Users\\Admin\\Desktop\\Module4Work\\most_watched_genres.png')
plt.show()


# Visualization 2: Distribution of Ratings and save the Image
plt.figure(figsize=(10, 6))
sns.histplot(netflix_data_cleaned['rating'], bins=30, kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.savefig('C:\\Users\\Admin\\Desktop\\Module4Work\\Distribution_of_ratings.png')
plt.show()

library(png)
library(grid)

chart_image <- readPNG("most_watched_genres.png")
grid.raster(chart_image)