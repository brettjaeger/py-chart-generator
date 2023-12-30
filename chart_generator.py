import plotly.express as px
import pandas as pd

input("Please collect your columns in the clipboard")

graph_type = input("Graph type: Scatter=s Line=l [s,l] ")
include_origin = input("Do you want the graph to include the origin? [Y/n]") or 'y'

data = pd.read_clipboard(sep='\t') #create dataset in pandas
try:
    if graph_type == 's':
        fig = px.scatter(data, x=data.columns[0], y=data.columns[1], color=data.columns[2], symbol=data.columns[2])
    elif graph_type == 'l':
        fig = px.line(data, x=data.columns[0], y=data.columns[1], color=data.columns[2], symbol=data.columns[2])
    else:
        print("Graph type error")
    # Set up axes to include origin
    if include_origin == 'y':
        fig.update_xaxes(rangemode='tozero')
    fig.show()
except IndexError:
    if graph_type == 's':
        fig = px.scatter(data, x=data.columns[0], y=data.columns[1])
    elif graph_type == 'l':
        fig = px.line(data, x=data.columns[0], y=data.columns[1])
    else:
        print("Graph type error")   
    # Set up axes to include origin
    if include_origin == 'y':
        fig.update_xaxes(rangemode='tozero')
    fig.show() 

