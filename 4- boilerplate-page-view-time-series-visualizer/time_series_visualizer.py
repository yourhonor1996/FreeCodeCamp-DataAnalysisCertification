import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col= 'date', parse_dates= True )

# Clean data
dropped = df.loc[(df['value'] <= df['value'].quantile(0.025)) | \
                 (df['value'] >= df['value'].quantile(0.975))]
df = df.drop(dropped.index)

figSize = (20, 9)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize= figSize)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.plot(df.index, df['value'], color= 'red')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df.index.year
    df_bar['month'] = df.index.month

    month_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']
    # Draw bar plot
    fig, axs = plt.subplots(figsize= (10,10))
    sns.barplot(x= 'year', y= 'value', hue= 'month', data= df_bar,
                palette= 'bright', ax= axs, ci= None)
    axs.legend(month_labels, loc= 'upper left')
    axs.set_ylabel('Average Page Views')
    axs.set_xlabel('Years')
    axs.set_xticklabels(axs.get_xticklabels(), rotation = 90)
    # catplt = sns.catplot(x= 'year', y= 'value', hue= 'month', kind= 'bar',
    #                      data= df_bar, legend_out= False, ci= None, palette= 'bright')
    # catplt.set(xlabel= 'Years', ylabel= 'Average Page Views')
    # catplt._legend.set_title('Month')
    
    
    # for t, l in zip(catplt._legend.texts, month_labels): t.set_text(l)
    # sns.despine(fig=catplt.fig, top=False, right=False, left=False, bottom=False, trim= False)
    # catplt.set_xticklabels(rotation= 90)

    # fig = catplt.fig
    # plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize= figSize)
    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x= 'year', y= 'value', palette= 'bright', data= df_box, ax= ax1)
    sns.boxplot(x= 'month', y= 'value', palette= 'bright', data= df_box, ax= ax2, order= month_labels)
    ax1.set_ylabel('Page Views')
    ax1.set_xlabel('Year')
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax2.set_ylabel('Page Views')
    ax2.set_xlabel('Month')
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
