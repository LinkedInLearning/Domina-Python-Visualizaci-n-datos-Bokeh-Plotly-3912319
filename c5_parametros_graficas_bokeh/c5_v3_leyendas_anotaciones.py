import numpy as np

from bokeh.plotting import figure, show
from bokeh.models import Label, Arrow, NormalHead, Span, BoxAnnotation


x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)


fig = figure()

fig.line(x, y1, legend_label="Sin(x)", line_color="blue")
fig.line(x, y2, legend_label="Cos(x)", line_color="green")

fig.legend.title = "Funciones"
fig.legend.location = "top_left"
fig.legend.orientation = "horizontal"

label = Label(x=2, y=0, text="(2, 0)")
fig.add_layout(label)

arrow = Arrow(end=NormalHead(size=10), x_start=0, y_start=0, x_end=0.5, y_end=0.5)
fig.add_layout(arrow)

span = Span(location=-1, dimension="width", line_color="green", line_width=2)
fig.add_layout(span)

box = BoxAnnotation(left=0, right=np.pi, bottom=0, top=1, fill_color='orange', fill_alpha=0.3)
fig.add_layout(box)

show(fig)
