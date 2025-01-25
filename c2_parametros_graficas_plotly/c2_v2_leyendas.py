import plotly.graph_objects as go

x_list = [1, 2, 3, 4, 5]
y_list = [10, 11, 12, 13, 14]

coordinates = [f"({x}, {y})" for x, y in zip(x_list, y_list)]

fig = go.Figure(
    data=go.Scatter(
        x=x_list,
        y=y_list,
        text=coordinates,
        mode="lines+markers+text",
        textposition="top center",
        name="Línea azul",
    )
)

fig.update_layout(
    title="Gráfico de Líneas",
    xaxis_title="Eje X",
    yaxis_title="Eje Y",
    legend=dict(
        title="Leyenda",
        x=0.75,
        y=0.95,
        bgcolor="rgba(255, 255, 255, 0.7)",
        bordercolor="black",
        borderwidth=2               
    ),
    showlegend=True
)

fig.show()

