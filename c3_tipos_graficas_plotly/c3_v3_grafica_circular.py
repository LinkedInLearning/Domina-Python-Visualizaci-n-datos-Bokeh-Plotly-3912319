import pandas as pd
import plotly.graph_objects as go

pnn_df = pd.read_csv("data/pnn_col.csv")
pnn_region_count = pnn_df.groupby("region").size().reset_index(name="cantidad")

fig = go.Figure(
    data=go.Pie(
        labels=pnn_region_count["region"],
        values=pnn_region_count["cantidad"],
        hole=0.2,
    ),
)

fig.update_traces(
    hoverinfo="value",
    textinfo="label+percent",
)

fig.show()
