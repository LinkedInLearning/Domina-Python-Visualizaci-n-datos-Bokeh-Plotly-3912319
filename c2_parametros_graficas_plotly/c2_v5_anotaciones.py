import plotly.graph_objects as go

x_list = [1, 2, 3, 4, 5]
y_list = [10, 11, 12, 13, 14]

coordinates = [f"({x}, {y})" for x, y in zip(x_list, y_list)]

fig = go.Figure(
    data=go.Scatter(
        x=x_list,
        y=y_list,
        mode="lines+markers",
    )
)

fig.add_annotation(
    x=x_list[1],
    y=y_list[1],
    text="Anotación",
    showarrow=True,
    arrowhead=4,
    arrowwidth=2,
    arrowcolor="gray",
    bordercolor="purple",
    borderwidth=2,
    bgcolor="white",
    font=dict(
        family="Arial",
        size=16,
        color="black"
    ),
)

fig.show()
