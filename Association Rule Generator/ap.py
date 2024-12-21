import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Prepare Transactional Data
# Example dataset: A list of transactions where each transaction is a list of items bought together
transactions = [
    ['milk', 'bread', 'butter'],
    ['bread', 'butter', 'jam'],
    ['milk', 'bread'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter', 'jam'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter', 'jam'],
]

# Step 2: Convert Data to One-Hot Encoding
# Create a DataFrame with one-hot encoding for each item in the dataset
# The index represents the transaction, and each column represents a product/item.
df = pd.DataFrame(transactions)
df = df.stack().str.get_dummies().groupby(level=0).sum()

# Convert to boolean values (True/False)
df = df.astype(bool)

# Step 3: Run Apriori Algorithm
# Set minimum support threshold (e.g., 0.4 means 40% of transactions must contain the itemset)
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

# Step 4: Generate Association Rules
# Set minimum threshold for confidence (e.g., 0.7 means 70% confidence for association)
# Also, specify the 'num_itemsets' argument for the association_rules function
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7, num_itemsets=2)

# Step 5: Output Results
# Display the frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)

# Display the association rules
print("\nAssociation Rules:")
print(rules)
