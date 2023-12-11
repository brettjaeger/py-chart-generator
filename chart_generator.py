import plotly.express as px
import pandas as pd

input("Please collect your columns in the clipboard")
graph_type = input("Graph type: Scatter=s Line=l")

data = pd.read_clipboard(sep='\t')

if graph_type == 's':
    fig = px.scatter(data, x=data.columns[0], y=data.columns[1], color=data.columns[2], symbol=data.columns[2])
elif graph_type == 'l':
    fig = px.line(data, x=data.columns[0], y=data.columns[1], color=data.columns[2], symbol=data.columns[2])
else:
    print("Graph type error")
fig.show()

