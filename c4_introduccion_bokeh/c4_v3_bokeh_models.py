from bokeh.io import show
from bokeh.models import ColumnDataSource, HoverTool, Line, LinearAxis, Plot


x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 5, 9]

plot = Plot()

line = Line(x="x", y="y")
source = ColumnDataSource(data=dict(x=x, y=y))

plot.add_glyph(source, line)

xaxis = LinearAxis()
plot.add_layout(xaxis, "below")

yaxis = LinearAxis()
plot.add_layout(yaxis, "left")

hover = HoverTool()
hover.tooltips = [("X", "@x"), ("Y", "@y")]

plot.add_tools(hover)

show(plot)
