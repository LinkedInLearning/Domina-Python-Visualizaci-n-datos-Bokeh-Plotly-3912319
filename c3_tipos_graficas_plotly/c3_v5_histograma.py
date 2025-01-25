import numpy as np
import plotly.graph_objects as go

np.random.seed(1)
x_data = np.random.randn(500)
x1_data = np.random.randn(500) + 1

fig = go.Figure()

fig.add_trace(go.Histogram(x=x_data))
fig.add_trace(go.Histogram(x=x1_data))

fig.update_layout(barmode="overlay")
fig.update_traces(opacity=0.75)

fig.show()
