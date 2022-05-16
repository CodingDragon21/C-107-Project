import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv("c-107 data.csv")
avg = df.groupby(['student_id', 'level'], as_index = False)['attempt'].mean()


fig = px.scatter(avg, x = 'student_id', y = 'level', size = "attempt", color = "attempt")
fig.show()