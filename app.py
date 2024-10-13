import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# Dash uygulamasını başlat
app = dash.Dash(__name__)

# Örnek veri seti
np.random.seed(42)
df = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C', 'D'], size=500),
    'Value': np.random.randn(500),
    'Date': pd.date_range('2022-01-01', periods=500)
})

# Layout
app.layout = html.Div([
    html.H1('Gelişmiş Python Dash Uygulaması', style={'textAlign': 'center'}),

    html.Label('Kategori Seçimi'),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': i, 'value': i} for i in df['Category'].unique()],
        value='A'
    ),

    html.Label('Tarih Aralığı Seçimi'),
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=df['Date'].min(),
        end_date=df['Date'].max(),
        display_format='YYYY-MM-DD'
    ),

    dcc.Graph(id='line-chart'),

    html.Hr(),

    dcc.Graph(id='box-plot')
])

# Callback fonksiyonları
@app.callback(
    Output('line-chart', 'figure'),
    Output('box-plot', 'figure'),
    Input('category-dropdown', 'value'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date')
)
def update_graphs(selected_category, start_date, end_date):
    # Seçilen kategori ve tarih aralığına göre veri süzme
    filtered_df = df[(df['Category'] == selected_category) &
                     (df['Date'] >= start_date) & (df['Date'] <= end_date)]

    # Çizgi grafiği
    line_fig = px.line(filtered_df, x='Date', y='Value', title=f'{selected_category} Kategorisi - Zaman Serisi')

    # Box plot
    box_fig = px.box(filtered_df, y='Value', title=f'{selected_category} Kategorisi - Box Plot')

    return line_fig, box_fig

# Uygulamayı çalıştır
if __name__ == '__main__':
    app.run_server(debug=True)
server = app.server









