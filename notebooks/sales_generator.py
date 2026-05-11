import pandas as pd
import numpy as np

np.random.seed(20)

rows = 3000

regions = ['North', 'South', 'East', 'West']
products = ['Product A', 'Product B', 'Product C']

sales_df = pd.DataFrame({
    'Region': np.random.choice(regions, rows),
    'Product': np.random.choice(products, rows),
    'Revenue': np.random.randint(1000, 50000, rows),
    'Orders': np.random.randint(1, 20, rows)
})

sales_df['Average_Order_Value'] = (
    sales_df['Revenue'] / sales_df['Orders']
)

sales_df.to_csv('sales_data.csv', index=False)

print('Sales dataset created!')
