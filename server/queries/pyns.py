from flask_api import FlaskAPI, status
import json

pyns = json.loads(open('mockdata/mockdata.json').read())

# Loaded data into the DB
# Next step, build a few SQL Statements and retrieve the data from the DB

def get_all_pyns():
    return pyns, status.HTTP_200_OK

def get_pyn_by_id(pyn_id):
    if pyn_id:
        pyn = [pyn for pyn in pyns if pyn['pyn_id'] == pyn_id]
        if len(pyn) == 0:
            return status.HTTP_404_NOT_FOUND
        return pyn[0], status.HTTP_200_OK 
    else: 
        return pyns, status.HTTP_200_OK

def get_pyns_by_user_id(user_id):
    if user_id:
        pyn = [pyn for pyn in pyns if pyn['pyn_id'] == pyn_id]
        if len(pyn) == 0:
            return status.HTTP_404_NOT_FOUND
        return pyn[0], status.HTTP_200_OK 
    else: 
        return pyns, status.HTTP_200_OK