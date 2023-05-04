"""
pipeline 1 (extract raw data from reddit, process it to clean data, store to db1)
mongodb.py: contains functions that handle queries in and out of mongo db 
reddit.py: contains functions that return reddit data, calls preprocess helper function 
p1.py: calls reddit.py and mongodb.py 

Pipeline 2 (get cleaned data from db1, opinion mine, store model output to db2)
Mongodb.py: …
Sqlite.py: contains functions that handle queries in and out of sqlite db 
Model.py: contains opinion mining model 
P2: calls mongodb.py, sqlite.py, model.py 

Pipeline 3 (processed db2 to visualization)
Sqlite.py: …
visualize.py: contains functions that visualize data
streamlit.py: contains functions streamlit-related 
P3: calls sqlite.py, visualize.py, streamlit.py 

pipeline 4 (train and eval model on training set)
model.py: 
trian.py: trains model 

Misc: 

Main
Calls p1.py, p2.py, p3.py
"""