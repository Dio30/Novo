from tqdm import tqdm

#quero entregar para a cidade de Rio de Janeiro
import requests

import win32com.client as win32

#passo 1: pegar a lista de ceps
with open("ceps.txt", "r") as arquivo:
    ceps = arquivo.read()
ceps = ceps.split("\n")

#passo 2: pegar as informações de cada CEP
enderecos_entrega = []
for cep in tqdm(ceps):
    link = f'https://cep.awesomeapi.com.br/json/{cep}'
#passo 3: verificar se a cidade é Rio de Janeiro
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']
#passo 4: printar o cep e o bairro
    if cidade == "Rio de Janeiro":
        enderecos_entrega.append((cep, bairro))
print(enderecos_entrega)

outlook = win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)
email.To = "padilhadione1@gmail.com"
email.Subject = "Entregas para o Rio de Janeiro"
email.HTMLBody = f"""
<p>Segue a lista de endereços de entrega para o Rio de Janeiro</p>

<p>{enderecos_entrega}</p>

<p>ATT,</p>
<p>Dione R Padilha</p>
"""

email.Send()
print("Email Enviado")
