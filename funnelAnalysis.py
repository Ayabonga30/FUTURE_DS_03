import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. LOADING DATA
df = pd.read_csv(
    "2019-Nov.csv",
    nrows=500000, 
    usecols=["event_time", "event_type", "user_id", "category_code", "price"]
)

print("Data loaded!\n")
# 2. CLEANING DATA
print("Missing values:\n", df.isnull().sum(), "\n")

# Convert time
df['event_time'] = pd.to_datetime(df['event_time'])

# Fill missing category
df['category_code'] = df['category_code'].fillna("unknown")

# 3. BUILD CORRECT FUNNEL (USER-LEVEL):

# Group events per user
user_events = df.groupby('user_id')['event_type'].unique()

# Convert to stage flags
def get_stage(events):
    events = set(events)
    return pd.Series({
        'view': 'view' in events,
        'cart': 'cart' in events,
        'purchase': 'purchase' in events
    })

user_stages = user_events.apply(get_stage)

# Funnel counts
views = user_stages['view'].sum()
carts = user_stages[(user_stages['view']) & (user_stages['cart'])].shape[0]
purchases = user_stages[(user_stages['view']) & (user_stages['cart']) & (user_stages['purchase'])].shape[0]

print("=== FUNNEL RESULTS ===")
print("Views:", views)
print("Carts:", carts)
print("Purchases:", purchases)

# 4. CONVERSION RATES
view_to_cart = carts / views if views > 0 else 0
cart_to_purchase = purchases / carts if carts > 0 else 0
overall_conversion = purchases / views if views > 0 else 0

print("\n=== CONVERSION RATES ===")
print("View → Cart:", view_to_cart)
print("Cart → Purchase:", cart_to_purchase)
print("Overall:", overall_conversion)

# 5. FUNNEL TABLE
funnel = pd.DataFrame({
    'Stage': ['View', 'Cart', 'Purchase'],
    'Users': [views, carts, purchases]
})

funnel['Conversion'] = [
    None,
    carts / views,
    purchases / carts
]

funnel['Dropoff'] = [
    None,
    1 - (carts / views),
    1 - (purchases / carts)
    ]

print("\n=== FUNNEL TABLE ===")
print(funnel)

# 6. CATEGORY ANALYSIS
category_conversion = df.groupby(['category_code', 'event_type'])['user_id'].count().unstack()

# Fill missing values
category_conversion = category_conversion.fillna(0)

# Avoid division by zero
category_conversion['conversion_rate'] = np.where(
    category_conversion['view'] > 0,
    category_conversion['purchase'] / category_conversion['view'],0)

print("TOP CONVERTING CATEGORIES")
print(category_conversion.sort_values(by='conversion_rate', ascending=False).head())

print("WORST CONVERTING CATEGORIES")
print(category_conversion.sort_values(by='conversion_rate').head())

# 7. TIME ANALYSIs
df['date'] = df['event_time'].dt.date

daily = df.groupby(['date', 'event_type'])['user_id'].nunique().unstack().fillna(0)

daily.plot(figsize=(10,5))
plt.title("User Activity Over Time")
plt.xlabel("Date")
plt.ylabel("Users")
plt.show()

# 8. EXTRA METRIC
total_users = user_stages.shape[0]
converted_users = user_stages[user_stages['purchase']].shape[0]

print("EXTRA INSIGHT")
print("Total Users:", total_users)
print("Users who purchased:", converted_users)
print("Purchase Rate:", converted_users / total_users)

df_small = df.sample(300000, random_state=42)
df_small.to_csv("clean_funnel_data.csv", index=False)
print("File saved successfully!")