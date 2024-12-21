import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch webpage content
url = "https://www.imdb.com/chart/top"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Step 2: Extract movie titles and ratings
movies = []
ratings = []

# Extract movie titles
for movie in soup.select("td.titleColumn"):
    title = movie.a.text  # Extract the movie title
    movies.append(title)

# Extract ratings using the new class
for rating in soup.find_all("span", class_="ipc-rating-star--rating"):
    rate = rating.text  # Extract the rating
    ratings.append(float(rate))

# Step 3: Create a DataFrame
data = pd.DataFrame({
    "Movie": movies[:len(ratings)],  # Match the number of titles and ratings
    "Rating": ratings
})

# Step 4: Analyze the data
# Display the top 10 movies
print("Top 10 Movies:")
print(data.head(10))

# Step 5: Visualize the data
# Plot top 10 movies
top_10 = data.head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_10["Movie"], top_10["Rating"], color='skyblue')
plt.xlabel("Rating")
plt.title("Top 10 Movies on IMDB")
plt.gca().invert_yaxis()
plt.show()
