import numpy as np

from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource


def generate_sin(x):
    new_x = x + np.pi/8
    new_y = np.sin(x)
    return new_x, new_y


source = ColumnDataSource(data={"x": [], "y": []})

fig = figure(title="Datos en Tiempo Real", x_axis_label="X", y_axis_label="Y")
fig.line("x", "y", source=source, line_width=2, line_color="blue")

current_x = 0


def update_data():
    global current_x

    new_x, new_y = generate_sin(current_x)
    source.stream({"x": [new_x], "y": [new_y]})

    current_x = new_x


curdoc().add_periodic_callback(update_data, 1000)
curdoc().add_root(fig)
