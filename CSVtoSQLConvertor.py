import pandas as pd
import sqlite3
import os
from sqlalchemy import create_engine

engine = create_engine('sqlite://', echo=False)
winter_files=os.listdir("Data/Winter")
summer_files=os.listdir("Data/Summer")
winter_dfs=[]
summer_dfs=[]
for file in winter_files:
    filename="Data/Winter/"+file
    winter_dfs.append(pd.read_csv(filename))
for file in summer_files:
    filename="Data/Summer/"+file
    summer_dfs.append(pd.read_csv(filename))
# df=pd.read_csv("Data/Winter/albertville-1992.csv")

# df.to_sql("albertville-1992",con=engine,index_label="leaderboard_id",if_exists="append")
# print(engine.execute("SELECT COUNT(*) FROM albertville-1992").fetchall())
for i in range(len(winter_dfs)):
    table_name=winter_files[i].replace("-","")
    table_name=table_name.replace(".csv","")
    winter_dfs[i].to_sql(table_name,con=engine,index_label="leaderboard_id",if_exists="append")
for i in range(len(summer_dfs)):
    table_name=summer_files[i].replace("-","")
    table_name=table_name.replace(".csv","")
    summer_dfs[i].to_sql(table_name,con=engine,index_label="leaderboard_id",if_exists="append")
# print(engine.execute("SELECT * FROM turin2006").fetchall())