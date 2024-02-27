# Create a KFold object
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Get the train and test data from the first split from the shuffled KFold
train_data_split, test_data_split = next(kfold.split(heart_disease_df_X))

# Print out the number of datapoints in the train and test splits
print("Number of training datapoints in heart_disease_df_X:", len(train_data_split))
print("Number of training datapoints in split:", len(train_data_split))
print("Number of testing datapoints in split:", len(test_data_split))
