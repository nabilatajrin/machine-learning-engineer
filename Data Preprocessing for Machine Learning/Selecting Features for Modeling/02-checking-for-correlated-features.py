# Print out the column correlations of the wine dataset
print(wine.head())

# Drop that column from the DataFrame
wine = wine.drop("Flavanoids", axis=1)

print(wine.head())
