


import pandas as pd
from sqlalchemy import create_engine


""" 
search_data = pd.read_csv(“/Users/tobias/Dropbox/Repos_v1/SashaStuff/searchResults.csv”,index_col=6, parse_dates=True)

engine = create_engine(‘mysql+pymysql://root:arlanda1@localhost:3306/test’)
#engine = create_engine(db_connect_string)
con = engine.connect()
df.to_sql(name=‘fpt_ordersTest’,con=con,if_exists=‘replace’, index = False)

"""