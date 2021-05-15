#%%
import numpy as np
from numpy.core.fromnumeric import sort
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline
# %%
sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date'])
# %%
sales.head()
# %%
sales.describe()
# %%
sales.columns
# %%
customer_data = sales['Customer_Age']
# %%
customer_data.plot(kind= 'kde')
# %%
sales['Country'].value_counts().plot(kind= 'bar', figsize= (14,6))
# %%
sales['Product_Category'].value_counts()
# %%
sales['Product'].value_counts()

# %%
sales['Product'].unique()

# %%
sales['Product'].value_counts(sort= True).head(10).plot(kind= 'bar', xlabel= 'things')
# %%
sales.plot(kind= 'scatter', x= 'Unit_Cost', y= 'Unit_Price', figsize= (6,6))
# %%
sales.plot(kind= 'scatter', x= 'Order_Quantity', y= 'Profit', figsize= (8,8));
# %%
sales[['Profit', 'Country']].boxplot (by='Country', figsize= (10,6))
# %%
sales[['Customer_Age', 'Country']].boxplot(by= 'Country', figsize= (12,8), )
# %%
sales.boxplot(column= 'Customer_Age', by= 'Country', figsize= (10,10))
# %%
sales['Product'].value_counts().head(10).plot(kind= 'bar', figsize= (8,8))
# %%
sales.plot(kind= 'scatter', x= 'Unit_Cost', y= 'Unit_Price', figsize= (8,8))
# %%
sales.corr()
# %%
sales[['Unit_Price', 'Unit_Cost']].corr()
# %%
sales.plot(kind= 'scatter', x= 'Order_Quantity', y= 'Profit', figsize= (7,7))
# %%
sales.boxplot('Profit', 'Country', figsize= (7,7))
# %%
sales.boxplot('Customer_Age', 'Country', figsize= (10,7))
# %%
sales['Calculated_Date'] = sales[['Year', 'Month', 'Day']].apply(lambda x: f'{x[0]}-{x[1]}-{x[2]}', axis= 1)
# %%
sales['Calculated_Date'].head()
# %%
sales['Calculated_Date'] = pd.to_datetime(sales['Calculated_Date'])
# %%
sales['Calculated_Date'].head()

# %%
sales['Calculated_Date'].value_counts().plot(kind= 'line', figsize= (20,8))
# %%
sales['Revenue'] += 50
sales['Revenue'].head(10)
# %%
sales.loc[(sales['Country'] == 'Canada') | (sales['Country'] == 'France')].shape[0]
# %%
sales.loc[(sales['Country'] == 'Canada') & (sales['Sub_Category'] == 'Bike Racks')].shape[0]
# %%
france_states = sales.loc[(sales['Country'] == 'France'), 'State'].value_counts()
# %%
france_states.plot(kind= 'bar', figsize= (10,7))
# %%
sales['Product_Category'].value_counts().plot(kind= 'pie', figsize= (8,8))
# %%
accessories = sales.loc[sales['Product_Category'] == 'Accessories', 'Sub_Category'].value_counts()
accessories
# %%
accessories.plot(kind= 'pie', figsize= (7,7))
# %%
bikes = sales.loc[sales['Product_Category'] == 'Bikes', 'Sub_Category'].value_counts()
bikes
# %%
bikes.plot(kind= 'pie', figsize= (7,7))

# %%
sales['Customer_Gender'].value_counts().plot(kind= 'bar', figsize= (5,10))
# %%
sales.loc[(sales['Customer_Gender'] == 'M') & (sales['Revenue'] > 500)].shape[0]

# %%
sales.sort_values('Revenue', ascending= False).head(5)
# %%
sales.loc[sales['Revenue'] == sales['Revenue'].max()]
# %%
sales.loc[sales['Revenue'] > 10000, 'Order_Quantity'].mean()
# %%
