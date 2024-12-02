from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('datasets/2/customer_shopping_data.csv')

app = Dash()

app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),

    dcc.Dropdown(df.gender.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(

    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph(value):
    dff = df[df['gender'] == value]

    # Generate a histogram for the filtered data
    return px.histogram(dff, x='price', nbins=200)

if __name__ == '__main__':
    app.run(debug=True)