import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

# here's the list of possible columns to choose from.
list_of_columns =['code', 'state', 'category', 'total exports', 'beef', 'pork', 'poultry',
       'dairy', 'fruits fresh', 'fruits proc', 'total fruits', 'veggies fresh',
       'veggies proc', 'total veggies', 'corn', 'wheat', 'cotton']

list_of_exports = ['total exports', 'beef', 'pork', 'poultry',
       'dairy', 'fruits fresh', 'fruits proc', 'total fruits', 'veggies fresh',
       'veggies proc', 'total veggies', 'corn', 'wheat', 'cotton']

mycolumn='corn'
#myheading1 = f"Wow! That's a lot of {mycolumn}!"
mygraphtitle = '2011 US Agriculture Exports by State'
mycolorscale = 'ylorrd' # Note: The error message will list possible color scales.
mycolorbartitle = "Millions USD"
tabtitle = 'Old McDonald'
sourceurl = 'https://plot.ly/python/choropleth-maps/'
githublink = 'https://github.com/austinlasseter/dash-map-usa-agriculture'


########## Set up the chart

import pandas as pd
df = pd.read_csv('assets/usa-2011-agriculture.csv')

def update_graph(myColumn):
       
       #global myheading1
       #myheading1 = f"Wow! That's a lot of {myColumn}!"
       
       fig = go.Figure(data=go.Choropleth(
              locations=df['code'], # Spatial coordinates
              z = df[myColumn].astype(float), # Data to be color-coded
              locationmode = 'USA-states', # set of locations match entries in `locations`
              colorscale = mycolorscale,
              colorbar_title = mycolorbartitle,
              ))

       fig.update_layout(
              title_text = mygraphtitle,
              geo_scope='usa',
              width=1200,
              height=800
              )
       return fig

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(mygraphtitle),
    dcc.Dropdown(
        id='my-dropdown',
        options=list_of_exports,
        value=list_of_exports[4],
        ),
    dcc.Graph(
        id='figure-1',
        figure=update_graph(mycolumn)
    ),

    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

@app.callback(Output('figure-1', 'figure'),
       Input('my-dropdown','value')
       )
def update_graph_callback(value):
       return update_graph(value)

############ Deploy
if __name__ == '__main__':
    app.run_server()
