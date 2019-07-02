from bokeh.models import HoverTool, ColumnDataSource
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    year = [1960, 1970, 1980, 1990, 2000, 2010]
    pop_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
    pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]

    output_file('line.html', mode='inline')
    plot = figure(title='Population Graph of India and Pakistan', x_axis_label='Year',
                  y_axis_label='Population in million')

    source_pk = ColumnDataSource(data=dict(
        year=year,
        population=pop_pakistan,
    ))

    source_in = ColumnDataSource(data=dict(
        year=year,
        population=pop_india,
    ))

    hover = HoverTool()
    hover.tooltips = """
    <div style=padding=5px>Year:@year</div>
    <div style=padding=5px>Population:@population</div>
    """
    plot.add_tools(hover)

    plot.line('year', 'population', line_width=2, line_color='green', legend='Pakistan', source=source_pk)
    plot.circle('year', 'population', fill_color="green", line_color='green', size=8, source=source_pk)

    plot.line('year', 'population', line_width=2, line_color='orange', legend='India', source=source_in)
    plot.circle('year', 'population', fill_color="orange", line_color='orange', size=8, source=source_in)
    show(plot)
