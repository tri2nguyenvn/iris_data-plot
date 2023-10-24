# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:53:45 2023

@author: baniyaghoubm
"""
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from mpl_toolkits.mplot3d import Axes3D
from plotly.subplots import make_subplots
from plotly.offline import plot
import plotly.express as px

# Load the Iris dataset
url = "iris.csv"
iris_data = pd.read_csv(url)
# Scatter Plot: Sepal Width vs. Sepal Length

plt.figure(figsize=(8, 6))
figure1= plt.scatter(iris_data["sepal_length"], iris_data["sepal_width"], color='red')
plt.title("Scatter Plot: Sepal Width vs. Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.grid(True)
plt.show()

# Line Chart: Petal Length over Species ID

plt.figure(figsize=(8, 6))

species_ids = range(len(iris_data))
figure2= plt.plot(species_ids, iris_data["petal_length"], color='blue')
plt.title("Line Chart: Petal Length over Species ID")
plt.xlabel("Species ID")
plt.ylabel("Petal Length")
plt.grid(True)
plt.show()

# Bar Chart: Species Distribution

species_counts = iris_data["species"].value_counts()
plt.figure(figsize=(8, 6))
figure3= plt.bar(species_counts.index, species_counts.values, color='lightpink')
plt.title("Bar Chart: Species Distribution")
plt.xlabel("Species")
plt.ylabel("Count")
plt.grid(axis='y')
plt.show()

# Pie Chart: Species Distribution as a percentage
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.figure(figsize=(8, 6))
figure4 = plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', colors=colors)
plt.title("Pie Chart: Species Distribution as a percentage")
plt.show()

# 3D Scatter Plot: 3D visualization of sepal length, sepal width, and petal length
fig = plt.figure(figsize=(10, 8))

ax = fig.add_subplot(111, projection='3d')
ax.scatter(iris_data["sepal_length"], iris_data["sepal_width"], iris_data["petal_length"], color='green')
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Sepal Width")
ax.set_zlabel("Petal Length")
ax.set_title("3D Scatter Plot: Sepal Length, Sepal Width, and Petal Length")
plt.show()


fig = make_subplots(rows=2, cols=2, shared_xaxes=False, shared_yaxes=False, start_cell="bottom-left",
                    specs = [[{'type': 'xy'}, {'type':'xy'}],
                             [{'type':'bar'}, {'type': 'pie'}]],
                    subplot_titles=("Scatter Plot: Sepal Width vs. Sepal Length","Line Chart: Petal Length over Species ID",
                                    "Bar Chart: Species Distribution","Pie Chart: Species Distribution as a percentage"))

fig.add_trace(go.Scatter(x = iris_data['sepal_length'],y = iris_data['sepal_width'])
             , row=1, col=1)


fig.add_trace(go.Scatter(x = iris_data["species"], y = iris_data["petal_length"])
              , row=1, col=2)
fig.add_trace(go.Bar(x = species_counts.index, y = species_counts.values),
              row=2, col=1)
fig.add_trace(go.Pie(values=species_counts.values, labels=species_counts.index),
              row=2, col=2)


plot(fig)





