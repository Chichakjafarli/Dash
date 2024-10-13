import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Məlumatları əl ilə daxil edin
data = {
    'Country': ['China', 'India', 'USA', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico'],
    'Population': [1439323776, 1380004385, 331002651, 273523615, 220892340, 212559417, 206139589, 164689383, 145934462, 128932753],
    'Region': ['Asia', 'Asia', 'North America', 'Asia', 'Asia', 'South America', 'Africa', 'Asia', 'Europe', 'North America']
}

# DataFrame yaradın
df = pd.DataFrame(data)

# Dash tətbiqini yaradın
app = dash.Dash(__name__)

# Dashboard layout-u
app.layout = html.Div(children=[
    html.H1(children='Advanced World Population Dashboard'),
    html.Label("Select a region:"),
    dcc.Dropdown(
        id='region-dropdown',
        options=[
            {'label': 'All Regions', 'value': 'All'},
            {'label': 'Asia', 'value': 'Asia'},
            {'label': 'North America', 'value': 'North America'},
            {'label': 'South America', 'value': 'South America'},
            {'label': 'Africa', 'value': 'Africa'},
            {'label': 'Europe', 'value': 'Europe'}
        ],
        value='All'
    ),
    html.Label("Select a chart type:"),
    dcc.Dropdown(
        id='chart-type',
        options=[
            {'label': 'Bar Chart', 'value': 'bar'},
            {'label': 'Pie Chart', 'value': 'pie'},
            {'label': 'Line Chart', 'value': 'line'},
            {'label': 'Heatmap', 'value': 'heatmap'}
        ],
        value='bar'
    ),
    html.Label("Select population range:"),
    dcc.RangeSlider(
        id='population-slider',
        min=df['Population'].min(),
        max=df['Population'].max(),
        step=1000000,
        value=[df['Population'].min(), df['Population'].max()],
        marks={int(i): f'{i//1000000}M' for i in range(df['Population'].min(), df['Population'].max(), 200000000)}
    ),
    html.Label("Search by country:"),
    dcc.Input(id='country-search', type='text', placeholder='Enter country name', debounce=True),
    dcc.Graph(id='population-graph'),
    dcc.Graph(id='average-population-line'),
    dcc.Graph(id='region-country-count'),
    html.H2("Population Data Table"),
    html.Table(id='population-table')
])

# Callback funksiyası
@app.callback(
    [Output('population-graph', 'figure'),
     Output('population-table', 'children'),
     Output('average-population-line', 'figure'),
     Output('region-country-count', 'figure')],
    [Input('region-dropdown', 'value'),
     Input('chart-type', 'value'),
     Input('population-slider', 'value'),
     Input('country-search', 'value')]
)
def update_graph_and_table(selected_region, selected_chart, population_range, search_country):
    filtered_df = df[(df['Population'] >= population_range[0]) & (df['Population'] <= population_range[1])]
    if search_country:
        filtered_df = filtered_df[filtered_df['Country'].str.contains(search_country, case=False, na=False)]
    if selected_region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    if selected_chart == 'bar':
        fig = px.bar(filtered_df, x='Country', y='Population', color='Region')
    elif selected_chart == 'pie':
        fig = px.pie(filtered_df, names='Country', values='Population')
    elif selected_chart == 'line':
        fig = px.line(filtered_df, x='Country', y='Population')
    elif selected_chart == 'heatmap':
        fig = go.Figure(data=go.Heatmap(z=filtered_df['Population'], x=filtered_df['Country'], y=filtered_df['Region'], colorscale='Viridis'))
    avg_population_df = df.groupby('Region').mean().reset_index()
    avg_pop_fig = px.line(avg_population_df, x='Region', y='Population')
    country_count_df = df.groupby('Region').count().reset_index()
    country_count_fig = px.bar(country_count_df, x='Region', y='Country')
    table_header = [html.Tr([html.Th("Country"), html.Th("Population"), html.Th("Region")])]
    table_body = [html.Tr([html.Td(row['Country']), html.Td(f"{row['Population']:,}"), html.Td(row['Region'])]) for _, row in filtered_df.iterrows()]
    table = table_header + table_body
    return fig, table, avg_pop_fig, country_count_fig

# Gunicorn üçün server obyektini göstərin
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
