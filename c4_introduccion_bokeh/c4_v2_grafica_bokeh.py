from bokeh.plotting import figure, show


x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 5, 9]

p = figure()
p.line(x, y)

show(p)
