import pandas as pd
import openpyxl
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACac31d90654ce3f95c9cecf9a01a6db89"
auth_token  = "a2c4355a8791e38d1e37e9a12ad0aab3"
client = Client(account_sid, auth_token)


# abrir e ler s arquivos
lista_arquivos = ['janeiro','fevereiro','março','abril','maio','junho']

for arquivo in lista_arquivos:
    arquivo = pd.read_excel(f'{arquivo}.xlsx')
    if (arquivo['Vendas'] > 55000).any():
        vendedor = arquivo.loc[arquivo['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = arquivo.loc[arquivo['Vendas'] > 55000,'Vendas'].values[0]
        print(f'alguem bateu a meta. O Vendedor: {vendedor},Vendas: {vendas}')
        message = client.messages.create(
            to="+55seu numero",
            from_="+16073337435",
            body="deu certo!")
        print(message.sid)
