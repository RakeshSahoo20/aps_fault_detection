import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH='/config/workspace/aps_failure_training_set1.csv'
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"


if __name__== "__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns:{df.shape}")


## now we convert the file into json so that we can dump this file into mango_db server 

df.reset_index(drop=True,inplace=True)  ## changes in same location
json_record=list(json.loads(df.T.to_json()).values())  ## convert csv files into json files
 ## we need only values so write there and json format converted into list shows one row

print(json_record[0])

## insert into mangodb

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)







