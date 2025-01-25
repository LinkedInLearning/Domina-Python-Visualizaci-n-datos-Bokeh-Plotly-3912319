import plotly.express as px

iris_df = px.data.iris()
fig_iris = px.scatter(
    iris_df,
    x="sepal_width",
    y="sepal_length",
    color="species"
)

fig_iris.show()
