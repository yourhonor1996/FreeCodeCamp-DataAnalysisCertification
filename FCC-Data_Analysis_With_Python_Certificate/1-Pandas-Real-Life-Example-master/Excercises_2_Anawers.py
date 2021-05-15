#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

%matplotlib inline
# %%
conn = sqlite3.connect('data/sakila.db')

df = pd.read_sql('''
    SELECT
        rental.rental_id, rental.rental_date, rental.return_date,
        customer.last_name AS customer_lastname,
        store.store_id,
        city.city AS rental_store_city,
        film.title AS film_title, film.rental_duration AS film_rental_duration,
        film.rental_rate AS film_rental_rate, film.replacement_cost AS film_replacement_cost,
        film.rating AS film_rating
    FROM rental
    INNER JOIN customer ON rental.customer_id == customer.customer_id
    INNER JOIN inventory ON rental.inventory_id == inventory.inventory_id
    INNER JOIN store ON inventory.store_id == store.store_id
    INNER JOIN address ON store.address_id == address.address_id
    INNER JOIN city ON address.city_id == city.city_id
    INNER JOIN film ON inventory.film_id == film.film_id
    ;
''', conn, index_col='rental_id', parse_dates=['rental_date', 'return_date'])
# %%
df.head()
# %%
df.shape

# %%
df['film_rental_duration'].mean()
# %%
df['film_rental_duration'].value_counts().plot(kind= 'bar', figsize= (8,8)),
df['film_rental_duration'].value_counts()
# %%
df.columns
# %%
df['film_rental_rate'].value_counts().plot(kind= 'bar', figsize= (7,7))
# %%
df['film_rental_rate'].value_counts().plot(kind= 'pie', figsize= (7,7))

# %%
df.boxplot('film_replacement_cost', vert= False)
# %%
df['film_replacement_cost'].plot(kind='box', vert=False, figsize=(14,6))
# %%
ax = df['film_replacement_cost'].plot(kind='density', figsize=(14,6), grid= True)
ax.axvline(df['film_replacement_cost'].mean(), color= 'red')
ax.axvline(df['film_replacement_cost'].median(), color= 'green')

# %%
plt.acorr(df['film_replacement_cost'])

# %%
df['film_rating'].value_counts().plot(kind= 'bar', figsize= (8,8), grid= True)
# %%
df.boxplot('film_replacement_cost', 'film_rating', figsize=(14,6), fontsize= 13, rot= 20, )
# %%
df['rental_days'] = df[['rental_date', 'return_date']].apply(lambda x: (x[1] - x[0]).days, axis=1)
df.head()
# %%
df['rental_days'].describe()
# %%
ax = df['rental_days'].plot(kind= 'density', figsize= (14,7))
ax.axvline(df['rental_days'].mean(), color= 'red')
# %%
df['film_daily_rental_rate'] = df['film_rental_rate'] / df['film_rental_duration']
df.head()
# %%
pic = df['film_daily_rental_rate'].plot(kind= 'density', figsize= (14,6))
pic.axvline(df['film_daily_rental_rate'].mean(), color= 'red')
# %%
df['film_daily_rental_rate'].sort_values(ascending= True).head(10)
# %%
df['film_daily_rental_rate'].value_counts()

# %%
df.loc[df['film_daily_rental_rate'] == df['film_daily_rental_rate'].min()].head(10)
# %%
df.loc[df['film_daily_rental_rate'] == df['film_daily_rental_rate'].max()].head(10)
# %%
df.loc[df['rental_store_city'] == 'Lethbridge'].shape
# %%
leth = df.loc[df['rental_store_city'] == 'Lethbridge', 'film_rating'].value_counts()
leth.plot(kind= 'bar', figsize= (14,6), title= 'Lethbridge Film Ratings', rot= 0)

# %%
# df.loc[(df['rental_store_city'] == 'Woodridge') & (df['film_rental_duration'] > 5), 'film_rating']
df.loc[(df['rental_store_city'] == 'Woodridge') & (df['film_rental_duration'] > 5)].shape[0]
# %%
df.head()
# %%
df.loc[(df['store_id'] == 2) | (df['film_replacement_cost'] < 10.99)].shape[0]
# %%
