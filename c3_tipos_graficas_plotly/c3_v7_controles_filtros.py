import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data/evaluaciones_agropecuarias_municipales_EVA_20241230.csv")
filtered_df = df.groupby(["GRUPO DE CULTIVO", "AÑO"]).size().reset_index(name="CANTIDAD")

year_list = sorted(filtered_df["AÑO"].unique())

fig = go.Figure()

for year in year_list:
    year_df = filtered_df[filtered_df["AÑO"] == year]

    fig.add_trace(
        go.Bar(
            x=year_df["GRUPO DE CULTIVO"],
            y=year_df["CANTIDAD"],
            visible=False,
        )
    )

fig.data[0].visible = True

slider_years = []
for i in range(len(year_list)):
    actual_year = year_list[i]
    year_data = dict(
        method="update",
        args=[{"visible": [False] * len(year_list)},
              {"title": f"Año: {str(actual_year)}"}],
        label=str(actual_year),
    )
    year_data["args"][0]["visible"][i] = True
    slider_years.append(year_data)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Año: "},
    pad={"t": 50},
    steps=slider_years
)]

fig.update_layout(
    sliders=sliders
)

fig.show()
