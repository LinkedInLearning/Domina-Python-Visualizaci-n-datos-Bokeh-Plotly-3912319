import pandas as pd
import plotly.graph_objects as go

pnn_df = pd.read_csv("data/pnn_col.csv")
pnn_region_count = pnn_df.groupby("region").size().reset_index(name="cantidad")
# pnn_region_count = pnn_df["region"].value_counts().reset_index(name="cantidad")
pnn_region_eco_count = pnn_df.groupby(["region", "ecoturismo"]).size().reset_index(name="cantidad")

fig = go.Figure(
    data=[
        go.Bar(
            x=group_df["region"],
            y=group_df["cantidad"],
            name=group,
        ) for group, group_df in pnn_region_eco_count.groupby("ecoturismo")
    ]
)

fig.update_layout(
    title="Cantidad de PNNs de Colombia por Región",
    xaxis=dict(
        title="Región"
    ),
    yaxis=dict(
        title="Cantidad de PNNs"
    ),
    barmode="stack"
)

fig.show()
