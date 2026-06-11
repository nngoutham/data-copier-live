import pandas as pd

def get_table(path):
    tables= pd.read_csv(path,sep=':')
    return tables.query("to_be_loaded=='yes'")