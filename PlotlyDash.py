import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

spacex_df = pd.read_csv("spacex_launch_geo.csv")
spacex_df.columns = spacex_df.columns.str.strip()

app = Dash(__name__)

launch_sites = spacex_df['Launch Site'].unique().tolist()
site_options = [{'label': 'All Sites', 'value': 'ALL'}] + [{'label': site, 'value': site} for site in launch_sites]

app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard", style={'textAlign': 'center', 'color': '#503D36'}),
    
    dcc.Dropdown(
        id='site-dropdown',
        options=site_options,
        value='ALL',
        placeholder='Select a Launch Site',
        searchable=True
    ),

    html.Br(),

    dcc.Graph(id='success-pie-chart'),

    html.Br(),

    html.P("Payload range (Kg):"),

    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=spacex_df['Payload Mass (kg)'].max(),
        step=1000,
        value=[0, spacex_df['Payload Mass (kg)'].max()],
        marks={0: '0', 1000: '1000', 5000: '5000', 10000: '10000'}
    ),

    dcc.Graph(id='success-payload-scatter'),
])

@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        fig = px.pie(spacex_df, names='Launch Site', title='Total Successful Launches by Site',
                     values='class')  # class = 1 means success
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        success_count = filtered_df['class'].value_counts().reset_index()
        success_count.columns = ['Outcome', 'Count']
        success_count['Outcome'] = success_count['Outcome'].replace({1: 'Success', 0: 'Failure'})
        fig = px.pie(success_count, names='Outcome', values='Count',
                     title=f'Success vs Failure for site: {selected_site}')
    return fig

@app.callback(
    Output('success-payload-scatter', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter(selected_site, payload_range):
    low, high = payload_range
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)

    if selected_site == 'ALL':
        filtered_df = spacex_df[mask]
    else:
        filtered_df = spacex_df[(spacex_df['Launch Site'] == selected_site) & mask]

    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title='Payload vs. Launch Outcome'
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)