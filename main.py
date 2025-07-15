import pandas as pd
import glob

csv_files = glob.glob("data/*.csv")  # adjust folder name or pattern as needed

# Read and combine them into one DataFrame
combined_df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

# Filter rows where 'product' column equals 'pink morsel' and make a copy to avoid warnings
filtered_df = combined_df[combined_df['product'] == 'pink morsel'].copy()
filtered_df['price'] = filtered_df['price'].str.replace('$', '', regex=False).astype(float)

# Calculate 'sales' column
filtered_df.loc[:, 'sales'] = filtered_df['price'] * filtered_df['quantity']

# Drop 'price' and 'quantity' columns
filtered_df = filtered_df.drop(columns=['price', 'quantity', 'product'])

filtered_df.to_csv('data/pink_morsel_formatted.csv', index=False)


# Show the result
print(filtered_df)
