# Define the marriage_year column
divorce["marriage_year"] = divorce['marriage_date'].dt.year
