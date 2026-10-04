import pandas as pd 

def load_sales_data(file_path):
    """ load sales data from a csv file """
    data = pd.read_csv(file_path)
    return data