from bokeh.models.annotations import Tooltip
from bokeh.models.sources import ColumnDataSource
from script import df 
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool

df["START_str"] = df["START"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["END_str"] = df["END"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)

p = figure(
            x_axis_type='datetime',
            height=300,
            width=1000,
            title='Motion Activity')

p.yaxis.minor_tick_line_color = None

hover = HoverTool(tooltips=[
                            ("Start","@START_str"),
                            ("End","@END_str")]
                            )

p.add_tools(hover)

q = p.quad(
            left='START', 
            right='END', 
            bottom=0, 
            top=1, 
            color='red',
            source=cds)

output_file('Graph.html')

show(p)




