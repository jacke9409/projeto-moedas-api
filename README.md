import streamlit as st
import requests
from datetime import datetime

st.title("💱 Cotação de Moedas - AwesomeAPI")

moedas = {
    "Dólar → Real": "USD-BRL",
    "Euro → Real": "EUR-BRL",
    "Bitcoin → Real": "BTC-BRL",
    "Libra → Real": "GBP-BRL"
}

opcao = st.selectbox("Selecione a moeda:", list(moedas.keys()))

if st.button("Buscar cotação"):
    url = f"https://economia.awesomeapi.com.br/json/last/{moedas[opcao]}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = list(dados.keys())[0]
        info = dados[chave]

        st.subheader(info["name"])
        st.write(f"**Alta do dia:** R$ {info['high']}")
        st.write(f"**Baixa do dia:** R$ {info['low']}")
        st.write(f"**Variação:** {info['varBid']}")
        st.write(f"**Cotação atual (compra):** R$ {info['bid']}")
        st.write(f"**Cotação atual (venda):** R$ {info['ask']}")

        hora = datetime.fromtimestamp(int(info["timestamp"]))
        st.caption(f"⏱️ Atualizado em: {hora.strftime('%d/%m/%Y %H:%M:%S')}")

        st.markdown("[🔗 Veja a documentação da API](https://docs.awesomeapi.com.br/api-de-moedas)")

    else:
        st.error("Erro ao buscar os dados da moeda. Tente novamente.")

        st.error("Erro ao buscar os dados da moeda. Tente novamente.")
