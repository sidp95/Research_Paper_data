import dash
import dash_html_components as html
import dash_core_components as dcc
from datetime import date

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        multi=True
    ),
    dcc.Dropdown(id='demo-dropdown2', multi = True),
    dcc.DatePickerRange(
        id='my-date-picker-range'),
    html.Div(id='dd-output-container'),
    html.Div(id='something')

])

@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    dash.dependencies.Output('demo-dropdown2', 'options'),
    dash.dependencies.Output('my-date-picker-range', 'min_date_allowed'),
    dash.dependencies.Output('my-date-picker-range', 'max_date_allowed'),
    [dash.dependencies.Input('demo-dropdown', 'value'),
    dash.dependencies.Input('demo-dropdown2', 'value')
    ])
def update_output(a,b):
    options=[
            {'label': 'tag1', 'value': 't1'},
            {'label': 'tag2', 'value': 't2'},
            {'label': 'tag3', 'value': 't3'}
        ]
    #date_picker = dcc.DatePickerRange(
    #    id='my-date-picker-range',
    min_date=date(2020, 1, 1)
    max_date=date(2021, 1, 1)
    #)
    #if (a is None) or (a == []):
    #    return 'You have selected "{}"'.format(b), val
    #elif (b is None) or (b == []):
    #    return 'You have selected "{}"'.format(a), val
    #else:
    #    return 'You have selected "{}"'.format(a), val
    return 'You have selected "{}" "{}"'.format(a,b), options, min_date, max_date



@app.callback(
    dash.dependencies.Output('something', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value'),
    dash.dependencies.Input('demo-dropdown2', 'value'),
    dash.dependencies.Input('my-date-picker-range', 'start_date'),
    dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_output2(team,tag,start, end):
    string_prefix = 'choices:  '

    missing_boolean = (start is not None) and (end is not None)

    if ((team is not None) and (team != [])) and ((tag is None) or (tag == [])):
        string_prefix +=  "only team, no tag"

        if missing_boolean:
            string_prefix = string_prefix + " and data ranges provided" + start

    elif ((tag is not None) and (tag != [])) and ((team is None) or (team == [])):
        string_prefix +=  "only tag, no team"

        if missing_boolean:
            string_prefix = string_prefix + " and data ranges provided"

    elif ((tag is None) or (tag == [])) and ((team is None) or (team == [])):
        string_prefix +=  "no team, no tag"

        if missing_boolean:
            string_prefix = string_prefix + " only date ranges provided" + start + " " + end
    else:
        string_prefix +=  "both team and tag selected"

        if missing_boolean:

            string_prefix = string_prefix + " and date ranges provided"





    #if (a is None) or (a == []):
    #    return 'You have selected "{}"'.format(b), val
    #elif (b is None) or (b == []):
    #    return 'You have selected "{}"'.format(a), val
    #else:
    #    return 'You have selected "{}"'.format(a), val
    return string_prefix


 

if __name__ == '__main__':
    app.run_server(debug=True)