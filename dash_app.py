from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


data = {'y': [2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022],
        'wk': [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
        'session_view': [0.0, 0.0, 47156.0, 46753.0, 5716.0, 10220.0, 20909.0, 23193.0, 17908.0,
                         12733.0, 19749.0, 24192.0, 21073.0, 9913.0],
        'hits_view': [0.0, 0.0, 98057.0, 93697.0, 7899.0, 13069.0, 30948.0, 34904.0, 25751.0, 16438.0,
                      25153.0, 30891.0, 27385.0, 12639.0],
        'adv_view_all': [0.0, 292.0, 12763.0, 34233.0, 765.0, 785.0, 3360.0, 3352.0, 2559.0,
                         0.0, 0.0, 0.0, 5.0, 0.0],
        'hits_tocart': [0.0, 0.0, 114.0, 66.0, 16.0, 12.0, 51.0, 45.0, 48.0, 44.0, 85.0, 62.0, 82.0, 19.0],
        'revenue': [0.0, 0.0, 14196.0, 13180.0, 6450.0, 3084.0, 11607.0, 15738.0, 12671.0, 8788.0,
                    12491.0, 25290.0, 13984.0, 6269.0],
        'ordered_units': [0.0, 0.0, 6.0, 13.0, 5.0, 2.0, 10.0, 12.0, 10.0, 6.0, 9.0, 20.0, 10.0, 3.0],
        'cancellations': [0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0],
        'returns': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 0.0, 0.0, 0.0, 0.0],
        'cpm': [0.0, 0.0, 76329.17785644531, 105793.49517822266, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'cpo': [0.0, 0.0, 76.32917785644531, 105.79349517822266, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}
df = pd.DataFrame.from_dict(data)

app = Dash(__name__)

app.layout = html.Div([
      dcc.Dropdown(options=['session_view', 'hits_view', 'adv_view_all', 'hits_tocart', 'revenue',
                            'ordered_units', 'cancellations', 'returns', 'cpm', 'cpo'],
                   value='session_view',
                   id='dropdown_columns',
                   ),
      dcc.Graph(id='line_plot'),
      ],
)


@app.callback(
    Output("line_plot", "figure"),
    Input("dropdown_columns", "value"))
def update_table_columns(column_name):
    fig = px.line(df, x='wk', y=column_name, title=f'{column_name} by week')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
