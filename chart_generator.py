import plotly.express as px
import pandas as pd

input("Please collect your columns in the clipboard")
graph_type = input("Graph type: Scatter=s Line=l [s,l] ")

data = pd.read_clipboard(sep='\t')
try:
    if graph_type == 's':
        fig = px.scatter(data, x=data.columns[0], y=data.columns[1], color=data.columns[2], symbol=data.columns[2])
        fig.show()
    elif graph_type == 'l':
        fig = px.line(data, x=data.columns[0], y=data.columns[1], color=data.columns[2], symbol=data.columns[2])
        fig.show()
    else:
        print("Graph type error")
except IndexError:
    if graph_type == 's':
        fig = px.scatter(data, x=data.columns[0], y=data.columns[1])
        fig.show()
    elif graph_type == 'l':
        fig = px.line(data, x=data.columns[0], y=data.columns[1])
        fig.show()
    else:
        print("Graph type error")    

