import requests

def pegar_preco_binance(crypto_pair):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={crypto_pair}'
    
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        preco = float(dados['price'])
        print(f'\033[33m{crypto_pair}: {preco:.2f} USD\033[0m')

        return preco
    else:
        print(f'Erro ao acessar a API. Status code: {resposta.status_code}')
        return None

precos = {}
pares = ['USDTBRL', 'XRPUSDT', 'SOLUSDT', 'ADAUSDT', 'ETHUSDT', 'SUIUSDT', 'LINKUSDT', 'FETUSDT', 'BTCUSDT']
for par in pares:
    preco = pegar_preco_binance(par)
    if preco is not None:
        precos[par] = preco

resp = input("Desejar converter BRL para alguma moeda? y/n\n:").lower()

if resp == "y":
    moeda = input("Qual moeda voce quer?\n:").upper()
    if f'{moeda}USDT' in precos: 
        valor = float(input("Quanto em BRL voce quer converter?\nR$"))
        valor /= precos['USDTBRL']
        preco_moeda = precos[f'{moeda}USDT']

        valor_convertido = valor / preco_moeda
        print(f'\n\033[33m${valor:.2f} equivale a {valor_convertido:.2f} {moeda}\033[0m')

    else:
        print(f"A moeda {moeda} não está na lista de pares disponíveis.")
else:
    print("Operação cancelada.")
