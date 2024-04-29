import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers

red_wine = pd.read_csv('red-wine.csv')

df_train = red_wine.sample(frac=0.7, random_state=0); df_valid = red_wine.drop(df_train.index)
# Scale to [0, 1]
max_ = df_train.max(axis=0); min_ = df_train.min(axis=0)
df_train = (df_train - min_) / (max_ - min_); df_valid = (df_valid - min_) / (max_ - min_)

X_train = df_train.drop("quality", axis=1); X_valid = df_valid.drop("quality", axis=1)
y_train = df_train['quality']; y_valid = df_valid['quality']

model = keras.Sequential([layers.Dense(512, activation='relu', input_shape=[11]),
                          layers.Dense(512, activation='relu'),layers.Dense(512, activation='relu'),
                          layers.Dense(1)])

model.compile( optimizer='adam', loss='mae')
history = model.fit(X_train, y_train, validation_data = (X_valid, y_valid), batch_size=256, epochs=10)
history_df = pd.DataFrame(history.history); history_df['loss'].plot()

plt.show()
