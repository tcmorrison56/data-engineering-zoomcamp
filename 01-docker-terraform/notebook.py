import pandas as pd
from sqlalchemy import create_engine

df = pd.read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet')

zones = pd.read_csv('https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv')


engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')

df.to_sql(name='green_taxi_data', con=engine, if_exists='replace')

zones.to_sql(name='zones', con=engine, if_exists='replace')




