from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go
import joblib
import datetime


def about(request):
    return render(request,'about.html')
def Home(request):
    
    df=pd.read_csv('daily_high.csv')
    df.Date=pd.to_datetime(df.Date)
    df.index=df['Date']
    
    fig = go.Figure()
    scatter = go.Scatter(x=df.index, y=df.High_Price,
                     mode='lines', name='test',
                     opacity=0.8, marker_color='green')
    fig.add_trace(scatter)
    plt_div = plot(fig, output_type='div')
    return render(request,'Home.html',context={'plt_div':plt_div})

def results(request):
    if request.method=='GET':
        days=int(request.GET['days'])
        model=joblib.load('model_final.sav')
        plt_div=days
        fore=model.forecast(days)
        fig = go.Figure()
        scatter = go.Scatter(x=fore.index, y=fore,
                     mode='lines', name='test',
                     opacity=0.8, marker_color='green')
        fig.add_trace(scatter)
        plt_div = plot(fig, output_type='div')
        return render(request,'results.html',context={'plt_div':plt_div,'days':days})

