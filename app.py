from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB], title='Data Scout FM')

layout = html.Div([html.H1('Hello World!')])

if __name__ == '__main__':
    app.run(debug=True, port=8050)
