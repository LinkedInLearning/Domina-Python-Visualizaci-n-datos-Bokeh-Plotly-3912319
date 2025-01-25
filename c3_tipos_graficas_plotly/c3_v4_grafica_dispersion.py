import numpy as np
import plotly.graph_objects as go


x = np.linspace(0, 10, 100)
y = 2 * x + np.random.normal(0, 2, x.shape)
size = np.random.randint(10, 30, 100)

fig = go.Figure(
    data=go.Scatter(
        x=x,
        y=y,
        mode="markers",
        marker=dict(size=size)
    )
)

fig.update_layout(
    xaxis=dict(title="x"),
    yaxis=dict(title="y"),
)

fig.show()
