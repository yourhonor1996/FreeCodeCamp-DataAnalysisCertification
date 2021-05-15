import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    X = df['Year']
    Y = df['CSIRO Adjusted Sea Level']
    END = 2051
    # Create scatter plot
    fig, axs = plt.subplots(figsize= (14,6))
    axs.scatter(X, Y)

    # Create first line of best fit
    
    line = linregress(X, Y)
    slope, intercept = line.slope, line.intercept

    X_line = range(1880, END)
    axs.plot(X_line, slope*X_line + intercept, color= 'red')
    
    # Create second line of best fit
    cond = df['Year'] >= 2000
    line2 = linregress(df.loc[cond, 'Year'] , df.loc[cond, 'CSIRO Adjusted Sea Level'])
    slope2, intercept2 = line2.slope, line2.intercept
    
    X_line2 = range(2000, END)
    axs.plot(X_line2, slope2*X_line2 + intercept2, color= 'black')
    

    # Add labels and title
    axs.set(xlabel = 'Year', ylabel= 'Sea Level (inches)', title= 'Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()