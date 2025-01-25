import plotly.graph_objs as go


months = ["Enero", "Febrero", "Marzo", "Abril", 
         "Mayo", "Junio", "Julio", "Agosto", 
         "Septiembre", "Octubre", "Noviembre", "Diciembre"]

min_temperature = [19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19]
max_temperature = [30, 30, 30, 30, 30, 30, 30, 31, 31, 29, 29, 29]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=months,
        y=min_temperature,
        name="Temperatura mínima",
        line=dict(color="blue", width=3),
    )
)

fig.add_trace(
    go.Scatter(
        x=months,
        y=max_temperature,
        name="Temperatura máxima",
        line=dict(color="red", width=3),
    )
)

fig.update_layout(
    title="Temperatura promedio de Cali, Colombia en 2024",
    xaxis=dict(
        title="Mes"
    ),
    yaxis=dict(
        title="Temperatura (grados centígrados)"
    ),
    showlegend=True,
)

fig.show()
