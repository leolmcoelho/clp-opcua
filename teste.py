import pandas as pd
import json
from datetime import datetime

# Nome do arquivo xlsx que você deseja ler
xlsx_file = "dados.xlsx"

# Leia o arquivo xlsx em um DataFrame
df = pd.read_excel(xlsx_file)

# Converta o DataFrame para JSON e oriente "records"
json_data = df.to_json(orient="records")

json_data = json.loads(json_data)
json_data = json_data[0]

# Imprima ou salve o JSON como desejar
# print(json_data[0].values())


def get_all_data():
    data = {}
    for i, tag in enumerate(json_data):

        data[tag] = json_data[key]
    data['DATA HORA'] = datetime.now()
    print(data)

def createDF(data):
    return pd.DataFrame([data])


for key in json_data.keys():
    data = {}
    for i, tag in enumerate(json_data.keys()):
        data[tag] = json_data[key]
    data['DATA HORA'] = datetime.now()
data = createDF(data)
print(data)




# Se você deseja salvar o JSON em um arquivo
# with open("dados.json", "w") as json_file:
#     json_file.write(json_data)
