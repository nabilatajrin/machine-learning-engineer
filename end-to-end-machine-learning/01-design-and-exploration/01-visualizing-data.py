# Print the first 5 rows of the DataFrame
print(heart_disease_df.head())

# Print information about the DataFrame
print(heart_disease_df.info())

# Visualize the cholestrol column
heart_disease_df['chol'].hist()

# Set the title and axis labels
plt.title('Cholestrol distribution')
plt.xlabel('Cholestrol')
plt.ylabel('Frequency')
plt.show()
