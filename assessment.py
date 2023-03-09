import pandas as pd

def transform(path1, path2):
    data = pd.read_csv("file.csv")
    data = data.drop_duplicates(subset="Name")
    data['Date']=pd.to_datetime(data['Date'])
    data['Date'] = data['Date'].dt.strftime('%d-%m-%Y')
    data = data.sort_values(by='Date', ascending = False)
    for i in data['Date']:
        if data['Date'].agg(['max'])[0] == i:
            data['Date'] = pd.Timestamp("today").strftime("%d-%m-%Y")
    data.to_csv(path2)
            
if __name__ == "__main__":
    path1 = 'file.csv'
    path2 = 'file_output.csv'
    transform(path1, path2)