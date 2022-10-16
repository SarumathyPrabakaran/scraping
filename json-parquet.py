from pyarrow import json
import pyarrow.parquet as pq

table = json.read_json('amazon.json') 
pq.write_table(table, 'data.parquet')
