import pandas as pd
import plotly.graph_objects as px

df = pd.read_csv('data.csv')

print(df.groupby('level')['attempt'].mean())

fig = px.Figure(px.Scatter(x = df.groupby('level')['attempt'].mean(), y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'], orientation = 'h'))
fig.show()