import dash
#import dash_core_components as dcc
from dash import dcc
from dash import html
from dash.dash_table.Format import Group
#import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import base64
from dash import dash_table
import io

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server
#### Carga Df vacio

##df = pd.read_csv('./datasets/blamk_SprinterOne.csv')



#### Definicion de Cards #####
# card_texto = dbc.Card(
#     [
#         dbc.CardBody([
#             html.H4("Datos del Sprint", className="card-title"),
#             #html.P("What was India's life expectancy in 1952?", className="card-text"),
#             dbc.ListGroup(
#                 [
#                     dbc.ListGroupItem("Distancia del Sprint [m]:"),
#                     dbc.ListGroupItem("Tiempo total [s]:"),
#                     dbc.ListGroupItem("Potencia promedio [Watt]:"),
#                     dbc.ListGroupItem("Ratio Potencia/Peso [Watt/Kg]:"),
#                     dbc.ListGroupItem("Gasto Energético total [kcal]:"),
                    
#                 ], flush=True)
#         ]),
#     ], color="warning",outline=True
# )

# card_value = dbc.Card(
#     [
#         dbc.CardBody([
#             html.H4("Valor ", className="card-title", style={'textAlign': 'right'}),
#             #html.P("What was India's life expectancy in 1952?", className="card-text"),
#             dbc.ListGroup(
#                 [
#                     # dbc.ListGroupItem(id='dist_sprint', children = 0),
#                     # dbc.ListGroupItem(id='tiempo_tot', children = 0),
#                     # dbc.ListGroupItem(id='pot_prom', children = 0),
#                     # dbc.ListGroupItem(id='ratio_pot_pes', children = 0),
#                     # dbc.ListGroupItem(id='gasto_energ', children = 0),
                    
#                     ############
#                     ############
                    
#                 ], flush=True, style={'textAlign': 'right'})
#         ]),
#     ], color="warning",outline=True
# )

# ###########
# card_texto_ = dbc.Card(
#     [
#         dbc.CardBody([
#             html.H4("Análisis del Sprint", className="card-title"),
#             #html.P("What was India's life expectancy in 1952?", className="card-text"),
#             dbc.ListGroup(
#                 [
#                     dbc.ListGroupItem("Distancia para alcanzar VEL MAX [m]:"),
#                     dbc.ListGroupItem("Distancia para alcanzar CAD MAX [m]:"),
#                     dbc.ListGroupItem("Tiempo para alcanzar MAX VEL [s]:"),
#                     dbc.ListGroupItem("Tiempo para alcanzar MAX CAD [s]:"),
#                     dbc.ListGroupItem("Tiempo sostenido a MAX VEL [s]:"),
#                     dbc.ListGroupItem("Tiempo sostenido a MAX CAD [s]:"),
                    
#                 ], flush=True)
#         ]),
#     ], color="warning",outline=True
# )

# card_value_ = dbc.Card(
#     [
#         dbc.CardBody([
#             html.H4("Valor", className="card-title", style={'textAlign': 'right'}),
#             #html.P("What was India's life expectancy in 1952?", className="card-text"),
#             dbc.ListGroup(
#                 [
#                     # dbc.ListGroupItem(id='dist_vel_max', children = 0),
#                     # dbc.ListGroupItem(id='dist_cad_max', children = 0),
#                     # dbc.ListGroupItem(id='time_vel_max', children = 0),
#                     # dbc.ListGroupItem(id='time_cad_max', children = 0),
#                     # dbc.ListGroupItem(id='time_sost_vel', children = 0),
#                     # dbc.ListGroupItem(id='time_sost_cad', children = 0),
                    
#                 ], flush=True, style={'textAlign': 'right'})
#         ]),
#     ], color="warning",outline=True
# )


#### Define Variables ######
markSegmentos = '''
## Selecciona un Segmento: 

- Selecciona un Sprint del menu desplegable 
para proceder con el análisis.
'''

# Define Colores

colors = {
    "graphBackground": "#F5F5F5",
    'background': '#f5fbfb',
    'text': '#038585'
}


#df = pd.read_csv('d:/PROYECTOS/DASHBOARDS/DASH/SprinterOne/datasets/goLabSprinterOne_3.csv')

features = ['TIME', 'SEGMENTO','MAXC','MAXV' , 'ODO', 'CADENCIA', 'VEL','ACC', 'POT_TRAB']



app.layout = html.Div([

    # DIV_1 Cabecera y Titulo
    html.Div([
                
                html.Div( html.Img(src=app.get_asset_url('/SprinterOne.png'),style={'height':'10%'}), style={'verticalAlign': 'top','width':'35%', 'float': 'rigth', 'display': 'inline-block'}
                    
                    ),


                html.Div([
                    dcc.Upload(
                        id='upload-data',
                        children=html.Div(
                            ["Arrastra o ", html.A("Haz Click")]),
                        style={
                            'width': '50%',
                            'verticalAlign': 'center',
                            'float': 'center',
                            'display': 'inline-block',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '2px',
                            'borderStyle': 'dashed',
                            'background': '#f6861f',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'color': '#ffffff',
                            'margin': 'auto'
                        },
                        # Permite multiples files  para uploaded
                        multiple=True),
                    ], style={'verticalAlign': 'center','width':'30%', 'float': 'rigth', 'display': 'inline-block'}),
                
                html.Div([dcc.Dropdown(id='selec_seg')], style={'verticalAlign': 'top','width':'20%', 'float': 'rigth', 'display': 'inline-block'}),
                html.Div( html.Img(src=app.get_asset_url('/golab.png'),style={'height':'10%'}), style={'verticalAlign': 'top','width':'15%','float': 'rigth', 'horizontalAlign':'center', 'display': 'inline-block'}
                    
                    ),

            ], style={
        'fontFamily': 'helvetica',
        'textAlign': 'left',
        'color': '#038585',
        'borderColor': 'gray',
        'borderWidth': '1px',
        'borderStyle': 'solid',
        'padding': 10, 
        'marginBottom': 5,
        'marginTop': 5} 


            ),


    # DIV_1 y 2 Carga Segmentos

    html.Div([
        
         html.Div( dcc.Graph(id='cadscore-graf',style={'align': 'top'}),        style={'verticalAlign': 'top','width':'30%', 'float': 'rigth', 'display': 'inline-block','fontFamily': 'helvetica',
        'color': '#038585',
        'borderColor': 'gray',
        'borderWidth': '1px',
        'borderStyle': 'solid',
        'verticalAlign': 'top',
        'position': 'top',}),
         # html.Div( dcc.Graph(id='velscore-graf'),        style={'verticalAlign': 'top','width':'25%', 'float': 'rigth', 'display': 'inline-block'}),

        
         html.Table(className='table',
                children = 
                [
                    html.Tr( [html.Th('Atributo'), html.Th("Valor"), html.Th("Unidad")] )
                ] +
                [
                    html.Tr( [html.Td('Distancia del Sprint:'),     html.Td(id='dist_segm', children = 0),    html.Td(' [m]')]),
                    html.Tr( [html.Td('Tiempo total:'),             html.Td(id='tiemp_tot', children = 0),     html.Td(' [s]')] ),
                    html.Tr( [html.Td('Potencia promedio:'),        html.Td(id='potencia_prom', children = 0),       html.Td(' [Watt]')] ),
                    html.Tr( [html.Td('Ratio Potencia/Peso:'),      html.Td(id='ratio_pot_pes', children = 0),  html.Td(' [Watt/Kg]')] ),
                    html.Tr( [html.Td('Gasto Energético total:'),   html.Td(id='gasto_energ', children = 0),    html.Td(' [kcal]')] ),
                ],style={'padding': 10,'verticalAlign': 'top','width':'35%', 'float': 'rigth', 'display': 'inline-block'}
            ),

       
        html.Table(className='table',
                children = 
                [
                    html.Tr( [html.Th('Atributo'), html.Th("Valor"), html.Th("Unidad")] )
                ] +
                [
                    html.Tr( [html.Td('Distancia para alcanzar VEL MAX:'),  html.Td(id='dist_vel_max', children = 0),   html.Td(' [m]')] ),
                    html.Tr( [html.Td('Distancia para alcanzar CAD MAX:'),  html.Td(id='dist_cad_max', children = 0),   html.Td(' [m]')] ),
                    html.Tr( [html.Td('Tiempo para alcanzar MAX VEL:'),     html.Td(id='time_vel_max', children = 0),   html.Td(' [s]')] ),
                    html.Tr( [html.Td('Tiempo para alcanzar MAX CAD:'),     html.Td(id='time_cad_max', children = 0),   html.Td(' [s]')] ),
                    html.Tr( [html.Td('Tiempo sostenido a MAX VEL:'),       html.Td(id='time_sost_vel', children = 0),  html.Td(' [s]')] ),
                    html.Tr( [html.Td('Tiempo sostenido a MAX CAD:'),       html.Td(id='time_sost_cad', children = 0),  html.Td(' [s]')] ),
                ],style={'verticalAlign': 'top','width':'35%', 'float': 'rigth', 'display': 'inline-block'}
            ),
 

    ], style={
        'fontFamily': 'helvetica',
        'color': '#038585',
        'borderColor': 'gray',
        'borderWidth': '1px',
        'borderStyle': 'solid',
        'padding': 10, 
        'marginBottom': 5,
        'marginTop': 5,
        'verticalAlign': 'top',
        'position': 'top',}

    ),

    # DIV_4 y 5 Carga Gauges y Calculos
  

                    # Gauge Scores Cad:Score y Vel.Score
    html.Div([
               
               
                        html.Div( dcc.Graph(id='gauge-vel-prom'), style={'width':'25%', 'float': 'right', 'display': 'inline-block'}),
                                                
                        html.Div( dcc.Graph(id='gauge-cad-max'), style={'width':'25%', 'float': 'rigth', 'display': 'inline-block'}),
                                                
                        html.Div( dcc.Graph(id='gauge-vel-max'), style={'width':'25%', 'float': 'right', 'display': 'inline-block'}),
                        
                        html.Div( dcc.Graph(id='gauge-cad-prom'), style={'width':'25%', 'float': 'right', 'display': 'inline-block'}),

                        

                         ],
                        style={
                        'fontFamily': 'helvetica',
                        'textAlign': 'left',
                        'color': '#038585',
                        'borderColor': 'ligth gray',
                        'borderWidth': '1px',
                        'borderStyle': 'solid',
                        'textAlign': 'left',
                        'padding': 1,
                        'marginBottom': 5,
                        'marginTop': 5}

                            
            ),




    # DIV_6_7 Graficos de Velocidad y Cadencia
    html.Div([
        
                    html.Div([
                        html.H5("Progresión de Cadencia v/s Odómetro", style={'textAlign':'center'}),
                        dcc.Graph(id='graf_cad')], style={'width':'46%', 'float': 'rigth', 'display': 'inline-block','height':'auto'}
                        ),
                    html.Div([
                        html.H5("Progresión de Velocidad v/s Odómetro", style={'textAlign':'center'}), 
                        dcc.Graph(id='graf_vel')], style={'width':'46%', 'float': 'rigth', 'display': 'inline-block','height':'auto'}),
      
    ], style={
        'fontFamily': 'helvetica',
        'textAlign': 'left',
        'color': '#038585',
        'borderColor': 'gray',
        'borderWidth': '1px',
        'borderStyle': 'solid',
        'padding': 10,
        'marginBottom': 5,
        'marginTop': 5}
    ),

        
    # DIV_6_7 Graficos de Velocidad y Cadencia
    html.Div([
        
                    html.Div([
                        html.H5("Progresión de Cadencia en el Tiempo", style={'textAlign':'center'}),
                        dcc.Graph(id='graf_time_cad')], style={'width':'46%', 'float': 'rigth', 'display': 'inline-block','height':'auto'}
                        ),
                    html.Div([
                        html.H5("Progresión de Velocidad en el TIempo", style={'textAlign':'center'}), 
                        dcc.Graph(id='graf_time_vel')], style={'width':'46%', 'float': 'rigth', 'display': 'inline-block','height':'auto'}),
      
    ], style={
        'fontFamily': 'helvetica',
        'textAlign': 'left',
        'color': '#038585',
        'borderColor': 'gray',
        'borderWidth': '1px',
        'borderStyle': 'solid',
        'padding': 10,
        'marginBottom': 5,
        'marginTop': 5}
    ),

    # DIV_10  Grafico */* con Dropdown
    html.Div([
        html.Div([
            html.H5('Eje X', style={'textAlign':'center'}),
            dcc.Dropdown(
                id='xaxis',
                options=[{'label': i.title(), 'value': i}
                         for i in features],

                value='ODO'
            )
        ], style={'width': '48%', 'display': 'inline-block','padding': 10, 'marginBottom': 15}),

        html.Div([
            html.H5('Eje y', style={'textAlign':'center'}),
            dcc.Dropdown(
                id='yaxis',
                options=[{'label': i.title(), 'value': i}
                         for i in features],
                value='VEL'
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block','padding': 10, 'marginBottom': 15}),

        html.H4('Explorador de Datos', style={'textAlign':'center'}),
        dcc.Graph(id='open-graph', style={'height': 600})
    ], style={
        'fontFamily': 'helvetica',
        'textAlign': 'left',
        'color': '#038585',
        'borderColor': 'gray',
        'borderWidth': '1px',
        'borderStyle': 'solid',
        'padding': 10,
        'marginBottom': 20,
        'marginTop': 15}),

    # DIV_11 Tabla Raw Data
    html.Div(id='tabla_raw', style={
        'fontFamily': 'helvetica',
        'textAlign': 'left',
        'color': '#038585',
                'borderColor': 'gray',
                'borderWidth': '1px',
                'borderStyle': 'solid',
                'padding': 10,
                'marginBottom': 5,
                'marginTop': 5})

], style={'padding': 10})


#######################
# Define Callbacks ####
#######################

# Open_graph


@app.callback(
    Output('open-graph', 'figure'),
    [Input('xaxis', 'value'),
     Input('yaxis', 'value'),
     Input('upload-data', 'contents'),
     Input('upload-data', 'filename'),
     Input('selec_seg', 'value')])
def open_graph(xaxis_name, yaxis_name, contents, filename, value):
    if contents:
        contents = contents[0]
        filename = filename[0]

        df = parse_contents(contents, filename)
        df = df.set_index(df.columns[0])
        
        dfs = df.loc[df['SEGMENTO'] == value] 
        
    ###########
        dfs.reset_index(inplace= True)
        dfs['ODO'] = dfs['ODO'] - dfs.loc[0,'ODO']
        dfs['TIME'] = (dfs['TIME'] - dfs.loc[0,'TIME']) / 1000
    ###########

    return {
        'data': [go.Scatter(
            x=dfs[xaxis_name],
            y=dfs[yaxis_name],
            text=dfs['SEGMENTO'],
            mode='markers',
            marker={
                'size': 8,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={'title': xaxis_name.title()},
            yaxis={'title': yaxis_name.title()},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


#Salida Gauge Max Cad
@app.callback(Output('gauge-cad-max', 'figure'),
              [Input('upload-data', 'filename'),
               Input('upload-data', 'contents'),
               Input('selec_seg', 'value')],)

def gaugeCadMax(filename, contents, value):
    if contents:
        contents = contents[0]
        filename = filename[0]

        df = parse_contents(contents, filename)
        df = df.set_index(df.columns[0])
        dfs = df.loc[df['SEGMENTO'] == value]


    figcadmax = go.Figure()
    
    figcadmax.add_trace(go.Indicator(
        mode="gauge+number+delta",
        value=dfs.CADENCIA.max(),
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Cadencia Máxima [RPM]", 'font': {'size': 24}},
        delta={'reference': df.CADENCIA.max(), 'increasing': {
            'color': "RebeccaPurple"}},
        gauge={
            'axis': {'range': [None, 260], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "white"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 100], 'color': '#808285'},
                {'range': [100, 200], 'color': '#537b7e'},
                {'range': [200, 220], 'color': '#f6861f'},
                {'range': [220, 260], 'color': '#f16139'}],
            'threshold': {
                'line': {'color': "white", 'width': 5},
                'thickness': 0.75,
                'value': df.CADENCIA.max()}}))


    return figcadmax

# Salida Gauge Prom Cad


@app.callback(Output('gauge-cad-prom', 'figure'),
              [Input('upload-data', 'filename'),
               Input('upload-data', 'contents'),
               Input('selec_seg', 'value')],)

def gaugeCadProm(filename, contents, value):
    if contents:
        contents = contents[0]
        filename = filename[0]

        df = parse_contents(contents, filename)
        df = df.set_index(df.columns[0])
        dfs = df.loc[df['SEGMENTO'] == value]


    figcadprom = go.Figure()
    
    figcadprom.add_trace(go.Indicator(
        mode="gauge+number+delta",
        value=dfs.CADENCIA.mean(),
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Cadencia Promedio [RPM]", 'font': {'size': 24}},
        delta={'reference': df.CADENCIA.mean(), 'increasing': {
            'color': "RebeccaPurple"}},
        gauge={
            'axis': {'range': [None, 260], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "white"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 100], 'color': '#808285'},
                {'range': [100, 200], 'color': '#537b7e'},
                {'range': [200, 220], 'color': '#f6861f'},
                {'range': [220, 260], 'color': '#f16139'}],
            'threshold': {
                'line': {'color': "white", 'width': 5},
                'thickness': 0.75,
                'value': df.CADENCIA.mean()}}))


    return figcadprom
# Salida Gauge Max Vel


@app.callback(Output('gauge-vel-max', 'figure'),
              [Input('upload-data', 'filename'),
               Input('upload-data', 'contents'),
               Input('selec_seg', 'value')],)
def gaugeVelMax(filename, contents, value):
    if contents:
        contents = contents[0]
        filename = filename[0]

        df = parse_contents(contents, filename)
        df = df.set_index(df.columns[0])
        dfs = df.loc[df['SEGMENTO'] == value]

    figvelmax = go.Figure()
    
    figvelmax.add_trace(go.Indicator(
        mode="gauge+number+delta",
        value=dfs.VEL.max(),
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Velocidad Máxima [Km/h]", 'font': {'size': 24}},
        delta={'reference': df.VEL.max(), 'increasing': {
            'color': "RebeccaPurple"}},
        gauge={
            'axis': {'range': [None, 75], 'tickwidth': 2, 'tickcolor': "darkblue"},
            'bar': {'color': "white"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 20], 'color': '#581845'},
                {'range': [20, 30], 'color': '#900c3f'},
                {'range': [30, 50], 'color': '#c70039'},
                {'range': [50, 75], 'color': '#ffc30f'}],
            'threshold': {
                'line': {'color': "white", 'width': 5},
                'thickness': 0.6,
                'value': df.VEL.max()}}))

    return figvelmax

# Salida Gauge Prom Vel


@app.callback(Output('gauge-vel-prom', 'figure'),
              [Input('upload-data', 'filename'),
               Input('upload-data', 'contents'),
               Input('selec_seg', 'value')],)
def gaugeVelProm(filename, contents, value):
    if contents:
        contents = contents[0]
        filename = filename[0]

        df = parse_contents(contents, filename)
        df = df.set_index(df.columns[0])
        dfs = df.loc[df['SEGMENTO'] == value]

    figvelmean = go.Figure()
    
    figvelmean.add_trace(go.Indicator(
        mode="gauge+number+delta",
        value=dfs.VEL.mean(),
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Velocidad Promedio [Km/h]", 'font': {'size': 24}},
        delta={'reference': df.VEL.mean(), 'increasing': {
            'color': "RebeccaPurple"}},
        gauge={
            'axis': {'range': [None, 75], 'tickwidth': 2, 'tickcolor': "darkblue"},
            'bar': {'color': "white"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 20], 'color': '#581845'},
                {'range': [20, 30], 'color': '#900c3f'},
                {'range': [30, 50], 'color': '#c70039'},
                {'range': [50, 75], 'color': '#ffc30f'}],
            'threshold': {
                'line': {'color': "white", 'width': 5},
                'thickness': 0.8,
                'value': df.VEL.mean()}}))

    return figvelmean

# Graf_VEL


@app.callback(Output('graf_vel', 'figure'),
              [Input('upload-data', 'contents'),
               Input('upload-data', 'filename'),
               Input('selec_seg', 'value')],
              )
def graf_vel(contents, filename, value):

    if contents:
        contents = contents[0]
        filename = filename[0]

        df = parse_contents(contents, filename)
        df = df.set_index(df.columns[0])
        
        dfs = df.loc[df['SEGMENTO'] == value]  
        dfs['DESCRIP'] = "Sprint: " + dfs['SEGMENTO'].map(str)
       
        dfs.reset_index(inplace= True)
        dfs['ODO'] = dfs['ODO'] - dfs.loc[0,'ODO']

    return {
        'data': [go.Scatter(
            x=dfs['ODO'],
            y=dfs['VEL'],
            text=dfs['DESCRIP'],
            mode='markers+lines',
            marker={
                'color':'#c70039',
                'size': 8,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={'title': 'Odómetro [m]'},
            yaxis={'title': 'Velocidad [Km/hr]'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }
# Graf_Time_Vel
@app.callback(Output('graf_time_vel', 'figure'),
              [Input('upload-data', 'contents'),
               Input('upload-data', 'filename'),
               Input('selec_seg', 'value')],
              )
def graf_time_vel(contents, filename, value):

    if contents:
        contents = contents[0]
        filename = filename[0]

        df = parse_contents(contents, filename)
        df = df.set_index(df.columns[0])
        
        dfs = df.loc[df['SEGMENTO'] == value]  
        dfs['DESCRIP'] = "Sprint: " + dfs['SEGMENTO'].map(str)
       
        dfs.reset_index(inplace= True)
        dfs['ODO'] = dfs['ODO'] - dfs.loc[0,'ODO']
        dfs['TIME'] = dfs['TIME'] - dfs.loc[0,'TIME']

    return {
        'data': [go.Scatter(
            y=dfs['VEL'],
            x=dfs['TIME']/1000,
            text=dfs['DESCRIP'],
            mode='markers',
            marker={
                'color':'#c70039',
                'size': 8,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            yaxis={'title': 'Velocidad [Km/h]'},
            xaxis={'title': 'Tiempo [s]'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


# Graf_CAD


@app.callback(Output('graf_cad', 'figure'),
              [Input('upload-data', 'contents'),
               Input('upload-data', 'filename'),
               Input('selec_seg', 'value')],
              )
def graf_cadencia(contents, filename, value):

    if contents:
        contents = contents[0]
        filename = filename[0]

        df = parse_contents(contents, filename)
        df = df.set_index(df.columns[0])
        
        dfs = df.loc[df['SEGMENTO'] == value]  
        dfs['DESCRIP'] = "Sprint: " + dfs['SEGMENTO'].map(str)
        
        dfs.reset_index(inplace= True)
        dfs['ODO'] = dfs['ODO'] - dfs.loc[0,'ODO'] # Resetea el Odometro para cada Sprint
        
   

    return {
        'data': [go.Scatter(
            x=dfs['ODO'],
            y=dfs['CADENCIA'],
            text= dfs['DESCRIP'],
            mode='markers+lines',
            name='Cadencia',
            marker={
                'color':'#537b7e',
                'size': 8,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={'title': 'Odómetro [m]'},
            yaxis={'title': 'Cadencia [RPM]'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }
# Graf_Time_cad

@app.callback(Output('graf_time_cad', 'figure'),
              [Input('upload-data', 'contents'),
               Input('upload-data', 'filename'),
               Input('selec_seg', 'value')],
              )
def graf_time_cad(contents, filename, value):

    if contents:
        contents = contents[0]
        filename = filename[0]

        df = parse_contents(contents, filename)
        df = df.set_index(df.columns[0])
        
        dfs = df.loc[df['SEGMENTO'] == value]  
        dfs['DESCRIP'] = "Sprint: " + dfs['SEGMENTO'].map(str)
       
        dfs.reset_index(inplace= True)
        dfs['ODO'] = dfs['ODO'] - dfs.loc[0,'ODO']
        dfs['TIME'] = dfs['TIME'] - dfs.loc[0,'TIME']

    return {
        'data': [go.Scatter(
            y=dfs['CADENCIA'],
            x=dfs['TIME']/1000,
            text=dfs['DESCRIP'],
            mode='markers',
            marker={
                'color':'#537b7e',
                'size': 8,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            yaxis={'title': 'Cadencia [RPM]'},
            xaxis={'title': 'Tiempo [s]'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }
# grafica Score
@app.callback(
    [Output('cadscore-graf', 'figure'), 
     Output('dist_vel_max', 'children'),
     Output('dist_cad_max', 'children'),
     Output('time_vel_max', 'children'),
     Output('time_cad_max', 'children'),
     Output('time_sost_vel', 'children'),
     Output('time_sost_cad', 'children'),],
    [Input('selec_seg','value'),
     Input('upload-data', 'contents'),
     Input('upload-data', 'filename')],
    )   #Output('velscore-graf', 'figure'),
def genera_score_tablas(value, contents, filename):

    if contents:
        contents = contents[0]
        filename = filename[0]

        df = parse_contents(contents, filename)
        df = df.set_index(df.columns[0])
        
        
        dfs = df.loc[df['SEGMENTO'] == value]
        dfs.reset_index(inplace=True)
        dfs['ODO'] = dfs['ODO'] - dfs.loc[0,'ODO']
        
            #############
    tiempoAntV = 0  # Para tener una referencia
    tiempoMaxVEL = 0
    odoAntV = 0
    odoMaxVEL = 0
    primerReg = True
    
    
    idxMaxV = dfs.VEL.idxmax(axis=0, skipna=True)
    maxVEL = dfs.loc[idxMaxV,'VEL']
    prcntVEL = maxVEL * 0.97  #conideraremos una velocidad igual al 3% menor que velocidad máxima para registrar el tiempo sobre ella como tiempo a velocidad máxima
    
    idxMaxC = dfs.CADENCIA.idxmax(axis=0, skipna=True)
    maxCAD = dfs.loc[idxMaxC,'CADENCIA']
    prcntCAD = maxCAD * 0.97
    
    
    for label, row in dfs.iterrows():
    
        if dfs.loc[label,'VEL'] >= prcntVEL:
            
            if primerReg == True:
                inicioVELmax = dfs.loc[label,'TIME']
                inicioODOmaxVEL = dfs.loc[label,'ODO']
                labelVELmax = label                 # indice del registro donde se produce el primer registros de prcntVEL
                primerReg = False
                
            tiempoMaxVEL = dfs.loc[label,'TIME'] -inicioVELmax  
            odoMaxVEL = dfs.loc[label,'ODO'] - inicioODOmaxVEL   
            tiempoAntV = dfs.loc[label,'TIME']
            odoAntV = dfs.loc[label,'ODO']

            
    
    primerReg = True        # Reseteamos primerReg
    tiempoAntC = 0
    tiempoMaxCAD = 0
    odoAntC = 0
    odoMaxCAD = 0
    
    for label, row in dfs.iterrows():
    
        if dfs.loc[label,'CADENCIA'] >= prcntCAD:
            
            if primerReg == True:
                inicioCADmax = dfs.loc[label,'TIME']
                inicioODOmaxCAD = dfs.loc[label,'ODO']
                labelCADmax = label                 # indice del registro donde se produce el primer registros de prcntVEL
                primerReg = False
                
            tiempoMaxCAD = dfs.loc[label,'TIME'] - inicioCADmax 
            tiempoAntC = dfs.loc[label,'TIME']
            odoMaxCAD = dfs.loc[label,'ODO'] - inicioODOmaxCAD 
            odoAntC = dfs.loc[label,'ODO']
            
    
    
    maxODO = dfs.loc[idxMaxV,'ODO']
    idxMaxT = dfs.TIME.idxmax(axis=0, skipna=True)
    maxTIME = dfs.loc[idxMaxT,'TIME'] - dfs.loc[0,'TIME']
    deltaTIME = maxTIME - dfs.loc[0,'TIME']
    
    velSCR =  (0.25*(maxTIME/(inicioVELmax - dfs.loc[0,'TIME']))+ 0.25*(tiempoMaxVEL/maxTIME)+ 0.5*(np.power((maxVEL/60 ),2))) * 100          #(datafrm.ODO.max() - odoMaxVEL) / datafrm.ODO.max()) * 100    
    cadSCR =  (0.25*(maxTIME/(inicioVELmax - dfs.loc[0,'TIME']))+ 0.25*(tiempoMaxCAD/maxTIME)+ 0.5*(np.power((maxCAD/230),2))) * 100 
    
    idxMaxC = dfs.CADENCIA.idxmax(axis=0, skipna=True)
    maxCAD = dfs.loc[idxMaxC,'CADENCIA']
    ############
    
    dist_max_vel = round(inicioODOmaxVEL, 2) #"Distancia para alcanzar VEL MAX:",
    dist_max_cad = round(inicioODOmaxCAD,2)#print("{:.2f}".format(inicioODOmaxCAD)) #Distancia para alcanzar CAD MAX:
    
    time_max_cad = round(((inicioCADmax - dfs.loc[0,'TIME']) / 1000),2) # "Tiempo para alcanzar MAX CAD:",
    time_max_vel = round(((inicioVELmax - dfs.loc[0,'TIME']) / 1000),2) #print("{:.2f}".format((inicioVELmax - dfs.loc[0,'TIME']) / 1000)) #"Tiempo para alcanzar MAX VEL:",
    time_sost_cad = round((tiempoMaxCAD / 1000),2) #"Tiempo sostenido a MAX CAD:",
    time_sost_vel = round((tiempoMaxVEL / 1000),2) #"Tiempo sostenido a MAX VEL:",
    

    
    ############
    fig_cad = go.Figure()
    #fig_vel = go.Figure()
    

    # fig_vel.add_trace(go.Indicator(
    #     mode = "gauge+number",
    #     value = velSCR, 
    #     #domain = {'x': [0.5, 0.75], 'y': [0.5, 0.75]},
    #     #domain = {'x': [0.5, 0.75], 'y': [0.5, 0.75]},
    #     gauge = {
    #         'axis': {'range': [None, 100]},
    #         'bar': {'color': "#c70039"},
    #     },
    #     number = {'valueformat': ".1f" },
    #     title = {'text': "VELScore"}),           
    #     )
    # fig_vel.update_layout(  # GET RID OF WASTE SPACE ON TOP OF GAUGES
    #         margin={'t': 0,
    #                 'b': 0,
    #                 'l': 0,
    #                 'r': 0},
    #         # height= 300,
    #         # width = 300
    #     )

    # fig_cad.add_trace(go.Indicator(
    #     mode = "gauge+number",
    #     value = cadSCR, 
    #     delta = {'reference': 100},
    #     # domain = {'x': [0, 0.25], 'y': [0.5, 0.75]},
    #     #domain = {'x': [0, 0.25], 'y': [0.25, 0.5]},
    #     gauge = {
    #         'shape': "angular",
    #         'axis': {'range': [None, 100]},
    #         'bar': {'color': "#537b7e"},
    #     },
    #     number = {'valueformat': ".1f" },
    #     title = {'text': "CADScore"}),           
    #     )
    # fig_cad.update_layout(  
    #         margin={'t': 0,
    #                 'b': 0,
    #                 'l': 0,
    #                 'r': 0},
    #         # height= 300,
    #         # width = 300
            
    #     )
    
    #######################
    #fig = go.Figure()
    
    fig_cad.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = velSCR,
        delta = {'reference': 100},
        domain = {'x': [0.25, 1], 'y': [0.08, 0.25]},
        title = {'text':"<b>VELScore</b><br><span style='color: gray; font-size:0.8em'>Ver. 1.0</span>", 'font': {"size": 16}},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': 50},
            'steps': [
                {'range': [0, 45], 'color': "#ffc30f"},
                {'range': [45, 75], 'color': "#f6861f"},
                {'range': [75, 100], 'color': "#f16139"}],
            'bar': {'color': "#c70039"}}))
    
    fig_cad.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = cadSCR,
        delta = {'reference': 100},
        domain = {'x': [0.25, 1], 'y': [0.4, 0.6]},
        title = {'text':"<b>CADScore</b><br><span style='color: gray; font-size:0.8em'>Ver. 1.1</span>", 'font': {"size": 16}},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': 50},
            'steps': [
                {'range': [0, 45], 'color': "#ffc30f"},
                {'range': [45, 75], 'color': "#f6861f"},
                {'range': [75, 100], 'color': "#f16139"}],
            'bar': {'color': "#537b7e"}}))
    
    # fig.add_trace(go.Indicator(
    #     mode = "number+gauge+delta", value = 220,
    #     delta = {'reference': 200},
    #     domain = {'x': [0.25, 1], 'y': [0.7, 0.9]},
    #     title = {'text' :"Satisfaction"},
    #     gauge = {
    #         'shape': "bullet",
    #         'axis': {'range': [None, 300]},
    #         'threshold': {
    #             'line': {'color': "black", 'width': 2},
    #             'thickness': 0.75,
    #             'value': 210},
    #         'steps': [
    #             {'range': [0, 150], 'color': "gray"},
    #             {'range': [150, 250], 'color': "lightgray"}],
    #         'bar': {'color': "black"}}))
    fig_cad.update_layout( margin = {'t':0})
    
    #######################

    return  fig_cad, dist_max_vel, dist_max_cad, time_max_vel, time_max_cad, time_sost_vel, time_sost_cad  #, fig_vel

# Carga Selector de Segmentos
@app.callback(
    [Output('selec_seg', 'value'),
     Output('selec_seg', 'options')],
    [Input('upload-data', 'contents'),
     Input('upload-data', 'filename')],
)
def genera_segmentos(contents, filename):

    if contents:
        contents = contents[0]
        filename = filename[0]

        df = parse_contents(contents, filename)
        df = df.set_index(df.columns[0])

    dfs = determinaSegmentos(df)

    options = [{'label': 'Sprint: ' + str(i), 'value': i} for i in dfs.SEGM]

    value = dfs.loc[0, 'SEGM']
    

    return value, options #, fig_cad, fig_vel


@app.callback(Output("tabla_raw", "children"),  # output-data-upload
              [Input("upload-data", "contents"),
               Input("upload-data", "filename")],)
def update_tabla_raw(contents, filename):
    table = html.Div()

    if contents:
        contents = contents[0]
        filename = filename[0]
        df = parse_contents(contents, filename)

        table = html.Div(
            [
                # html.H5(filename),
                dash_table.DataTable(
                    data=df.to_dict("rows"),
                    columns=[{"name": i, "id": i} for i in df.columns],
                    page_action='none',
                    style_table={'height': '300px',
                                 'width': 'auto',
                                 'overflowY': 'scroll',
                                 'tableAlign': 'auto'},
                    style_cell = {
                                'font_family': 'helvetica',
                                'font_size': '18px',
                                'text_align': 'center'},
                    tooltip={'SEGMENTO': 'Segmento N°' },
                    fixed_rows={'headers': True},
                ),
                html.Hr(),

            ]
        )

    return table

######### Calculo de Calorías y Trabajo del segmento ###########
@app.callback(
    [Output('dist_segm', 'children'),
     Output('gasto_energ', 'children'),
     Output('potencia_prom', 'children'),
     Output('ratio_pot_pes', 'children'),
     Output('tiemp_tot', 'children')],
    [Input('selec_seg','value'),
     Input('upload-data', 'contents'),
     Input('upload-data', 'filename')],
    )
def sprinterStats (value, contents, filename): #, cogDiam, cataDiam, biela, masaTotRider):
    
    if contents:
        contents = contents[0]
        filename = filename[0]

        df = parse_contents(contents, filename)
        df = df.set_index(df.columns[0])
        
        
        dfs = df.loc[df['SEGMENTO'] == value]
        dfs.reset_index(inplace=True)
        dfs['ODO'] = dfs['ODO'] - dfs.loc[0,'ODO']
        
    
    ###########
      # Revisar calculo del tiempo trabajado, considerando los tiempos a velocidad 0 de tl forma de 
      # no subreestimar el trabajo realizado y saber el tiempo total en moivimiento

    #### Datos del Datalog
    velAnt = dfs.VEL.iloc[0]                  # para tener un valor de referencia al inicio
    tiempoAnt = dfs.TIME.iloc[0]                # para tener un valor de referencia al inicio
    cadenciaAnt = dfs.CADENCIA.iloc[0]             # para tener un valor de referencia al inicio
    
    
    #### Variables y Constantes
    masaTotRider = 80
    acelTrab = 0                        # Aceleración del microsegmento en curso
    odoAnt = 0                          # Distancia recorrida en microsegmento anerior
    distTrab = 1.88 / 4                 # Mientras el Odometro
    coefRozamiento = 0.22
    acelAnterior = 0                   # Aceleración del microsegmento anterior
    #cadenciaAnt = 0
    tiempoDetenido = 0                  # Almacena el tiempo total a velocidad 0 [Km/hr]
    anguloSeg = 0                       # Angulo de PITCH de la bicicleta en el microsegmento
    acgrav = 9.8067                     # Aceleración de gravedad [m/seg2]
    distOdoMin = 1.88                   # Distancia de resolución Odometro Asociada al perímetro del neumático  [m]
    radioRueda = 0.3                    # radio de la Rueda de tracción [m]
    
    #### Factores Ambientales
    areaFrontal = 0.509                 # Area frontal rider en m2
    rho = 1.22601                       # densidad del aire en Kg/m3
    coefDrag = 0.63                     # Drag Coefficient Cd 0.6 a | 0.8 dependiendo de la posición de pedaleo
    coefResisRodado = 0.005             # Coeficiente de resistencia al rodado 0.0022 to 0.0050		Production bicycle tires at 120 psi (8.3 bar) and 50 km/h (31 mph), measured on rollers 
    perdidaDriveTrain = 0.02            # Resistencia por perdida en el drive train [%]
    
    #### Tabla de radios [m] de Piñones zn, Catalina czn y Biela  crank####
    cogDiam = 0.03657                   # para Piñón de 18 dientes 
    cataDiam = 0.08296                  # para Catalina de 41 dientes
    biela = 0.170                       # largo biela [m]


    #### Iterando en el Dataframe
    for label, row in dfs.iterrows():
    
            
        # Capturo el tiempo detenido considerando VEL <= 0.
        if dfs.loc[label,'VEL'] <= 0.:
            if label > 0:
                tiempoDetenido = (dfs.loc[label,'TIME'] - dfs.loc[(label-1),'TIME']) / 60000 + tiempoDetenido               # no puede restarse el valor de lista con indice -1
                dfs.loc[label,'TIEMPO_DET'] = tiempoDetenido
                
        
            
      
        #### Considerando un cambio en la velocidad se produce aceleración para efecto de los cálculos de potencia
        
        if dfs.loc[label,'CADENCIA'] > cadenciaAnt and dfs.loc[label,'VEL'] > velAnt:                                                                #(dfs.loc[label,'VEL'] distinto de 0 
            
            tiempoSeg = (dfs.loc[label,'TIME'] - tiempoAnt) / 1000                      # Tiempo en el microsegmento entre interrupciones [seg]
  
            distTrab  = (dfs.loc[label,'ODO'] - odoAnt)                                 # distTrab [m]
            acelTrab  = ((dfs.loc[label,'VEL'] /3.6) - (velAnt / 3.6)) / tiempoSeg      # Aceleración en el microsegmento entre interrupciones

            
            ####### Calculo de fuerza opuesta al movimiento (Fo)
            
            fuerzaDescompEjeX = masaTotRider * acgrav * np.sin(anguloSeg)
            fuerzaDescompEjeY = masaTotRider * acgrav * np.cos(anguloSeg)
            fuerzaRozam = coefRozamiento * fuerzaDescompEjeY 
            fuerzaOpuesta =  fuerzaRozam * (1 + perdidaDriveTrain) + fuerzaDescompEjeX      # masaTotRider * acelTrab +# + (0.5 * coefDrag * areaFrontal * rho * pow((dfs.loc[label,'VEL'] / 3.6),2))) * (dfs.loc[label,'VEL'] / 3.6)) / (1 - perdidaDriveTrain)                               # Revisar la aceleracion requerida en este punto.
            trabajo = (fuerzaOpuesta * distTrab)                                                                  # [N * m]Trabajo en el microsegmento                                                             # * np.cos(anguloSeg))      
            potencia = trabajo / tiempoSeg                                                                        # [Nm/s] Potencia en el microsegmento
            
            tiempoAnt = dfs.loc[label,'TIME']
            odoAnt =  dfs.loc[label,'ODO']
            velAnt = dfs.loc[label,'VEL']
            
             
                          #DEBUG FUNCION

            dfs.loc[label,'F_OPUESTA'] = fuerzaOpuesta

            dfs.loc[label,'DIST_TRAB'] = distTrab
            dfs.loc[label,'ACEL_TRAB'] = acelTrab
            dfs.loc[label,'POT_TRAB'] = potencia
            dfs.loc[label,'TRAB_JOULE'] = trabajo
            dfs.loc[label,'T_TRAB'] = tiempoSeg
      
       
        acelAnterior = acelTrab
        cadenciaAnt = dfs.loc[label,'CADENCIA']
        
        
    
    #dfs.ODO.iloc[0] = 0
    
    ###### Imprime Estadisticas #########
    dist_segm_ = round(((dfs.ODO.iloc[-1]-dfs.ODO.iloc[0])),2)
    gasto_energ_ = round((dfs.POT_TRAB.sum() * 0.000239),2)
   # potencia_prom_ = round(dfs.POT_TRAB.sum() / (dfs.ODO.max() / distOdoMin ),2)
    potencia_prom_ = round(dfs.POT_TRAB.max(),2)
    ratio_pot_pes_ = round(((dfs.POT_TRAB.sum() / (dfs.ODO.max() / distOdoMin )) / masaTotRider),2)
    #tiempo_movim = round((((dfs.TIME.iloc[-1]-dfs.TIME.iloc[0])/1000) - tiempoDetenido),2)
    tiemp_tot_ = round((((dfs.TIME.iloc[-1]-dfs.TIME.iloc[0])/1000)),2)
    
    return  dist_segm_, gasto_energ_, potencia_prom_, ratio_pot_pes_, tiemp_tot_


###############

#######################
# Define Funciones ####
#######################
# Esta funcion devuelve el DataFrame que se genera a partir del archivo .CSV



def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return df


def determinaSegmentos(datafrm):
    datafrm.drop_duplicates(subset=['SEGMENTO', 'PTIMEC', 'CADENCIA','MAXC', 'PTIMEV', 'VEL','MAXV', 'ODO'],keep='first', inplace= True)
    datafrm.reset_index(inplace = True)
    segmentos = pd.DataFrame(datafrm['SEGMENTO'].value_counts().reset_index().values, columns=["SEGM", "REGISTROS"])
    segmentos = segmentos.loc[segmentos['REGISTROS'] > 20]
    return segmentos

###############


if __name__ == '__main__':
    app.run_server(debug=False)
