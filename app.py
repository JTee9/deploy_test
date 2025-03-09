from dash import Dash, html

app = Dash(__name__, use_pages=True, title='Data Scout FM')
server = app.server

app.layout = html.Div([html.H1('Hello World!')])

if __name__ == '__main__':
    app.run(debug=True, port=8050)
