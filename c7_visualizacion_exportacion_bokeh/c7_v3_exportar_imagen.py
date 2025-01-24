import numpy as np

from bokeh.io import export_png, export_svg
from bokeh.plotting import figure


x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)


fig = figure()

fig.line(x, y1, legend_label="Sin(x)", line_color="blue")
fig.line(x, y2, legend_label="Cos(x)", line_color="green")

fig.legend.title = "Funciones"
fig.legend.location = "top_left"

export_png(fig, filename="grafico.png")
export_svg(fig, filename="grafico.svg")
