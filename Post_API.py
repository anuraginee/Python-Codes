import requests
import json
from Config import app_params
import pandas as pd

Host = app_params["host"]
Json = app_params["Json"]

def Read_CSV(Json):
    df = pd.read_csv(Json,encoding='latin1')

    JSON_Data = df.apply(lambda x: x.to_dict(), axis=1)
    headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            }
    for i in JSON_Data:
        print(i)

    print(len(JSON_Data))
    Sentence_scoring = []
    for i in JSON_Data:
        Input_Request = requests.post(Host,json=i,headers=headers)
        Output_Response = Input_Request.json()
        Sentence_scoring.append(Output_Response)
    print(f"The output response for Input_response is {Output_Response}")


