print("Hello!\nThis is a graph which represents student levels vs attempts.")
#importing the libraries
import csv
import pandas as pd
import plotly.express as px

#reading the file
df=pd.read_csv("studentLevels.csv")

#taking the data and then converting the series of data into a data frame by using "as_index=False" and then finding the mean.
mean=df.groupby(["Student_Id", "Level"], as_index=False)["Attempt"].mean()

#plotting the data into a scatter plot
fig=px.scatter(mean,x="Student_Id", y="Level", size="Attempt", color="Attempt", title="Student Levels vs Attempts")

#calling the function
fig.show()
