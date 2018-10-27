import plotly
import plotly.graph_objs as go
from py_expression_eval import Parser

parser = Parser()

minX = input("Minimum X value: ")
minX = int(minX)
maxX = input("Maximum X value: ")
maxX = int(maxX)

expression = input("Enter the equation of the graph from left to right (use ^ for powers): ")


def equation(x):
    try:
        result = parser.evaluate(expression, {'x': x})
        return result
    except:
        return "Error"


x_vals = []
y_vals = []

for i in range(minX, maxX):
    x_vals.append(i)

for i in x_vals:
    val = equation(i)    # takes in x vals from list and gets y result
    y_vals.append(val)

scatter_plot = go.Scatter(x=x_vals, y=y_vals)

plotly.offline.plot({
    "data": [scatter_plot],
    "layout": go.Layout(title="Cube Function")
}, auto_open=True)

