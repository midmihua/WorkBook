import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd


def show_graph(data):

    df = pd.DataFrame(data)
    print(df)

    trace = go.Candlestick(x=df[1],
                           open=df[2],
                           high=df[3],
                           low=df[4],
                           close=df[5])
    data = [trace]
    py.iplot(data)
