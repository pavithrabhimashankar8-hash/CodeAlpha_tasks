import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 60)
print("      CODEALPHA DATA ANALYTICS - TASK 3")
print("         DATA VISUALIZATION PROJECT")
print("=" * 60)

# Read CSV File
data = pd.read_csv("scraped_data.csv")

print("\nDataset Loaded Successfully")

# Display First 5 Rows
print("\nFirst 5 Records")
print(data.head())

# Rating Count
rating_count = data["Rating"].value_counts()

print("\nBook Rating Count")
print(rating_count)

# Graph Style
sns.set_style("whitegrid")

# Create Figure
plt.figure(figsize=(8,5))

# Bar Graph
sns.barplot(
    x=rating_count.index,
    y=rating_count.values,
    palette="viridis"
)

plt.title("Book Ratings Distribution")
plt.xlabel("Ratings")
plt.ylabel("Number of Books")

# Save Graph
plt.savefig("book_rating_graph.png")

# Show Graph
plt.show()

print("\nGraph Created Successfully")
print("Graph Saved as : book_rating_graph.png")

print("\nTask 3 Completed Successfully")
print("=" * 60)