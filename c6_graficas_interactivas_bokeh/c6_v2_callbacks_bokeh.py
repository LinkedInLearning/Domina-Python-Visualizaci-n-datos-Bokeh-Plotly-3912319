import numpy as np

from bokeh.layouts import layout
from bokeh.models import Slider
from bokeh.plotting import figure, curdoc


x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)


fig = figure(title="Sin(x)", x_axis_label="x", y_axis_label="sin(x)")

wave = fig.line(x, y, line_color="blue", line_width=2)

slider = Slider(start=1, end=10, value=2, step=0.1, title="Grosor de Línea")

def update_line_width(attr, old, new):
    wave.glyph.line_width = new

slider.on_change("value", update_line_width)


fig_layout = layout([
    [slider],
    [fig]
])

curdoc().add_root(fig_layout)
