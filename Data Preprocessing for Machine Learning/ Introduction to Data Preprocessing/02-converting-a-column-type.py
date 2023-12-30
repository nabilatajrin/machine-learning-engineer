# Print the head of the hits column
print(volunteer["hits"].dtypes)

# Convert the hits column to type int
volunteer["hits"] = volunteer["hits"].astype(int)

# Look at the dtypes of the dataset
print(volunteer.dtypes)
