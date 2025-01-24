import pandas as pd

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show


pnn_df = pd.read_csv("data/pnn_col.csv")
pnn_region_count = pnn_df.groupby("region").size().reset_index(name="cantidad")


source = ColumnDataSource(pnn_region_count)

fig = figure(x_range=pnn_region_count["region"], width=800, height=500)
fig.vbar(x="region", top="cantidad", source=source, width=0.8)

show(fig)
