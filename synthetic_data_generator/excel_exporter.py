import pandas as pd

def export_to_excel(data, filename="synthetic_data.xlsx"):
    df = pd.read_json(data)
    df.to_excel(filename, index=False)