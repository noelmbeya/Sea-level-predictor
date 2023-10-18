import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    x_future = np.arange(1880, 2051)
    best_fit_line = slope * x_future + intercept
    plt.plot(x_future, best_fit_line, color='red')

    # Create second line of best fit
    df2 = df.loc[df['Year']>= 2000]
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x2, y2)
    new_x_future = np.arange(2000, 2051)
    new_best_fit_line = slope * new_x_future + intercept
    plt.plot(new_x_future, new_best_fit_line, color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (Inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()