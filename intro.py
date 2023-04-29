import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)



app = Dash(__name__)

# ------------------------------------------------------------------------------SECTION OF DATA
# Import and clean data (importing csv into pandas)

dataset_file = "DataGruppo1.xlsx"
print('pippo')
df = pd.read_excel(dataset_file)
#df = df.groupby(['Year']).mean()
df.reset_index(inplace=True)
df['Date'] = '2/19/2016'
print(df)

# ------------------------------------------------------------------------------
# App layout
#go to: https://dash.plotly.com/dash-core-components
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016}],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_data_map', figure={})

])












# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)

