from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(
    rows=2,
    cols=1,
    subplot_titles=("Gráfica 1", "Gráfica 2"),
    row_heights=[0.7, 0.3],
)

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=[10, 20, 30], y=[4, 5, 6]),
    row=2, col=1
)

fig.show()
