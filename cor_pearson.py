#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path_file = 'data/MoviesOnStreamingPlatforms_updated.csv'
#%%
movies = pd.read_csv(path_file)
movies['Rotten Tomatoes'] = movies['Rotten Tomatoes'].str.replace("%", "").astype(float)
print(movies.head())
print(movies.dtypes)

# %%
movies.drop(["Type", 'Unnamed: 0'], axis=1, inplace=True) 

#%% 
movies.set_index('ID', inplace=True)

#%%
correlations = movies.corr()
# %%
print(correlations['Year'])

#%%
sns.heatmap(correlations)
plt.show()

### Sacado de: https://towardsdatascience.com/correlation-is-simple-with-seaborn-and-pandas-28c28e92701e