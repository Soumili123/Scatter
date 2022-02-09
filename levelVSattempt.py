import csv
import plotly.express as px

import numpy

with open("data.csv") as csv_file :
   
    df = csv.DictReader(csv_file)


  
    fig = px.scatter(df, x = "student_id",  y = "level")
    
    fig.show()