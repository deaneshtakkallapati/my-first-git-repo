from pathlib import Path
from warnings import simplefilter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.deterministic import DeterministicProcess, CalendarFourier
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
plt.rc("figure", figsize=(10, 5))
plot_params = dict(legend=True, style=".-", color="0.75")

fourier = CalendarFourier(freq="A", order=10)  # 10 sin/cos pairs for "A"nnual seasonality

dp = DeterministicProcess(
    index=tunnel.index,
    constant=True,               # dummy feature for bias (y-intercept)
    order=1,                     # trend (order 1 means linear)
    seasonal=True,               # weekly seasonality (indicators)
    additional_terms=[fourier],  # annual seasonality (fourier)
    drop=True,                   # drop terms to avoid collinearity
)

X = dp.in_sample()
y = tunnel["NumVehicles"]

model = LinearRegression(fit_intercept=False)
model.fit(X, y)

y_pred = pd.Series(model.predict(X), index=y.index)
X_fore = dp.out_of_sample(steps=90)
y_fore = pd.Series(model.predict(X_fore), index=X_fore.index)

ax = y.plot(color='0.25', style='.', title="Tunnel Traffic - Seasonal Forecast")
ax = y_pred.plot(ax=ax, label="Seasonal")
ax = y_fore.plot(ax=ax, label="Seasonal Forecast", color='C3')
_ = ax.legend()
plt.show()