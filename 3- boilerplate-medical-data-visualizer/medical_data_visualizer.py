import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df[['weight', 'height']].apply(
    lambda x: 1 if x[0]/pow(x[1]/100, 2) > 25 else 0 ,
    axis= 1)

# Normalize data by making 0 always good and 1 always bad. 
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0.
# If the value is more than 1, make the value 1.
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['gluc'] == 1, 'gluc'] = 0

df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] > 1, 'gluc'] = 1


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol','gluc', 'smoke', 'alco', 'active', and 'overweight'.
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    # You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df.melt(id_vars= 'cardio', value_vars= ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    
    # Draw the catplot with 'sns.catplot()'
    # fig, ax = plt.subplots(1, 2)
    fig = sns.catplot(x= 'variable', hue= 'value',col= 'cardio', kind = 'count', data= df_cat)
    fig.set_axis_labels('', 'total')
    fig.set_xlabels('variable')
    fig = fig.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    cond = \
        (df['ap_lo'] <= df['ap_hi']) & \
        (df['height'] >= df['height'].quantile(0.025)) & \
        (df['height'] <= df['height'].quantile(0.975)) & \
        (df['weight'] >= df['weight'].quantile(0.025)) & \
        (df['weight'] <= df['weight'].quantile(0.975))
    df_heat = df.loc[cond]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones(corr.shape)).astype(np.bool)


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize= (14,10))
    
    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data= corr, mask= mask, robust= False, annot= True, fmt= '.1f', ax= ax)
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
