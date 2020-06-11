# Importar pacotes necessários
import pandas as pd

from time import sleep
from whatsapp_api import WhatsApp

# Função para ler arquivos de Excel
df = pd.read_excel("nomes-para-bot-do-zap.xlsx")
df.head()
# df['Contato']
# df['Mensagem']

# Puxar dados do Excel
contatos = list(df['Contato'])
fake_news = list(df['Mensagem'])

primeiros_nomes = [n.split(' ')[0] for n in contatos]

# Inicializar o WhatsApp
wp = WhatsApp()

input("Precione enter após scanear o QR Code")
print('Iniciando...')

for contato, contato_pesquisar, fk \
    in zip(primeiros_nomes, contatos, fake_news):
    wp.search_contact(contato_pesquisar)
    sleep(2)
    
    mensagem = f"Olá {contato}! Essa é uma mensagem automatizada, estou criando um bot do zap zap."
    mensagem2 = f"A fakenews escolhida para você é *{fk}*."
    
    sleep(2)
    wp.send_message(mensagem)
    
    sleep(2)
    wp.send_message(mensagem2)
    
# Esperar 10 segundos e fechar
sleep(10)
print("Feito!")
wp.driver.close()