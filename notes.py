"""
pipeline 1 (extract raw data from reddit, store raw data to db1)
mongodb.py: contains functions that handle queries in and out of mongo db 
reddit.py: contains functions that return reddit data 
p1.py: calls reddit.py and mongodb.py 

Pipeline 2 (get raw data from db1, preprocess raw data to cleaned data, store to db2)
mongodb.py: … 
Preprocess.py: contains functions that preprocess raw db1 data
P2: calls mongodb.py and preprocess.py 

Pipeline 3 (get cleaned data from db2, opinion mine, store model output to db3)
Mongodb.py: …
Sqlite.py: contains functions that handle queries in and out of sqlite db 
Model.py: contains opinion mining model 
train.py: trains model 
P3: calls mongodb.py, sqlite.py, model.py 

Pipeline 4 (processed db3 to visualization)
Sqlite.py: …
visualize.py: contains functions that visualize data
streamlit.py: contains functions streamlit-related 
P4: calls sqlite.py, visualize.py, streamlit.py 

Misc: 

Main
Calls p1.py, p2.py, p3.py, p4.py 
"""