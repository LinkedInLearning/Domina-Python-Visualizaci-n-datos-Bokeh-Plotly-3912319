import numpy as np

from bokeh.layouts import column, layout
from bokeh.models import ColorPicker, Div, RangeSlider
from bokeh.plotting import figure, show


x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)


fig = figure(x_range=(0, np.pi), title="Sin(x)", x_axis_label="x", y_axis_label="sin(x)")

wave = fig.line(x, y, line_color="blue", line_width=2)

picker = ColorPicker(title="Color de Línea")
picker.js_link("color", wave.glyph, "line_color")

div = Div(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur at volutpat dui. Donec justo tortor, congue vitae mollis nec, tincidunt.",
    width=350,
    height=30,
)


range_slider = RangeSlider(
    start=0,
    end=6*np.pi,
    value=(1, np.pi),
    step=np.pi/4,
    title="Rango X"
)
range_slider.js_link("value", fig.x_range, "start", attr_selector=0)
range_slider.js_link("value", fig.x_range, "end", attr_selector=1)


fig_layout = layout([
    [div, picker],
    [range_slider],
    [fig]
])

show(fig_layout)
# show(column(picker, fig))
