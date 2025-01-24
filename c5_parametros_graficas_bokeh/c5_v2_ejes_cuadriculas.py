import pandas as pd

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show


pnn_df = pd.read_csv("data/pnn_col.csv")
pnn_region_count = pnn_df.groupby("region").size().reset_index(name="cantidad")


source = ColumnDataSource(pnn_region_count)

fig = figure(x_range=pnn_region_count["region"], width=800, height=500)
fig.vbar(x="region", top="cantidad", source=source, width=0.8)

fig.xaxis.axis_label = "Región"
fig.yaxis.axis_label = "Cantidad de PNNs"

fig.xaxis.axis_label_text_font = "Arial"
fig.xaxis.axis_label_text_font_style = "bold"
fig.xaxis.axis_label_text_font_size = "14pt"
fig.xaxis.major_label_orientation = "vertical"

fig.yaxis.axis_line_color = "red"
fig.yaxis.axis_line_width = 2
fig.yaxis.minor_tick_line_color = "purple"
fig.yaxis.minor_tick_line_width = 2
fig.yaxis.major_tick_line_color = "pink"
fig.yaxis.major_tick_line_width = 2

fig.ygrid.grid_line_color = "blue"
fig.ygrid.grid_line_alpha = 0.5
fig.ygrid.grid_line_dash = "dotted"

fig.xgrid.visible = False

show(fig)
