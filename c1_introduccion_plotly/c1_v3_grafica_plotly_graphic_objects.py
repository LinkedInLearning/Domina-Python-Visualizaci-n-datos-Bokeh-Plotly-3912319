import plotly.graph_objects as go

x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]

fig = go.Figure(
    data=go.Scatter(
        x=x,
        y=y,
        mode="lines",
        name="Ejemplo"
    )
)

fig.update_layout(
    title="Gráfico de Líneas",
    xaxis_title="Eje X",
    yaxis_title="Eje Y"
)

fig.show()
