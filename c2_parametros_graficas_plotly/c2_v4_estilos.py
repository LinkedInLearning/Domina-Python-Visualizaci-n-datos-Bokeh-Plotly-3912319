import plotly.graph_objects as go

x_list = [1, 2, 3, 4, 5]
y_list = [10, 11, 12, 13, 14]

coordinates = [f"({x}, {y})" for x, y in zip(x_list, y_list)]

fig = go.Figure(
    data=go.Scatter(
        x=x_list,
        y=y_list,
        mode="lines+markers",
        line=dict(color="purple", dash="dash", width=2),
        marker=dict(color="purple", size=15),
    )
)

fig.update_layout(
    title="Gráfico de la recta",
    title_x=0,
    title_font_family="Arial",
    title_font_color="red",
    xaxis=dict(
        title="Eje X",
        showgrid=True,
        gridcolor="white",
    ),
    yaxis=dict(
        title="Eje Y",
        showgrid=False,
    ),
    plot_bgcolor="gray",
    paper_bgcolor="lightgray",
)

fig.show()
