from pathlib import Path
from warnings import simplefilter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.deterministic import DeterministicProcess
from sklearn.linear_model import LinearRegression

simplefilter("ignore")
'''
  Read CSV File with parse_dates=Day, set index as Day
  Fill default values for plt.rc
  set moving_avg  to tunnel.rolling (window=365, center=True and min_periods=days/2+1)
  set ax to tunnel.plot()
  set ax in moving_avg.plot
  
'''
tunnel = pd.read_csv('tunnel.csv', parse_dates=["Day"])
tunnel = tunnel.set_index("Day").to_period()
plt.rc("figure", figsize=(10,5))
plot_params = dict(legend=True, style=".-", color="0.75")
global ax


def plot_moving_avg_for_tunnel_traffic():
    moving_avg = tunnel.rolling(center=True, window=365, min_periods=183).mean()
    ax = tunnel.plot(style=".", color="0.5")
    moving_avg.plot(ax=ax, linewidth=3, title="Moving 365 Days Traffic Data", legend=False)
    plt.show()


def plot_linear_traffic_trend():
    dp = DeterministicProcess(index=tunnel.index, constant=True, order=1, drop=True)
    X = dp.in_sample();
    y = tunnel['NumVehicles']
    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)
    y_pred = pd.Series(model.predict(X), index=X.index)
    ax = tunnel.plot(style=".", color="0.25", title="Tunnel Traffic - Linear Trend")
    _ = y_pred.plot(ax=ax, linewidth=3, label="Trend")
    plt.show()

def tunnel_trend_forecast():
    global ax
    dp = DeterministicProcess(index=tunnel.index, constant=True, order=1, drop=True)
    X = dp.in_sample()
    y = tunnel['NumVehicles']
    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)
    y_pred = pd.Series(model.predict(X), index=X.index)
    X = dp.out_of_sample(steps=20)
    y_forecast = pd.Series(model.predict(X), index=X.index)

    ax = tunnel["2005-05":].plot(title="Tunnel Traffic", **plot_params)
    ax = y_pred["2005-05":].plot(ax=ax, linewidth=3, label="Trend")
    ax = y_forecast.plot(ax=ax, linewidth=3, label="Trend Forecast", color="C3")
    _ = ax.legend()
    plt.show()

# plot_moving_avg_for_tunnel_traffic()
# plot_linear_traffic_trend()
tunnel_trend_forecast()





