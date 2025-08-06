import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("clwin_final.csv", index_col=0).head(10)
wins = df["wins"]
clubs = df["club"]
country = df["country"]

plt.pie(wins, labels=clubs );
plt.show();