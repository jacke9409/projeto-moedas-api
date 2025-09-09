import streamlit as st            # Importa o Streamlit para criar a interface web
import requests                  # Importa requests para fazer requisições HTTP

# Define o título da aplicação que será mostrado no topo da página
st.title("Cotação de Moedas - AwesomeAPI")

# Dicionário com as opções de moedas disponíveis para consulta
# A chave é o texto exibido para o usuário, o valor é o código usado na API
moedas = {
    "Dólar → Real": "USD-BRL",
    "Euro → Real": "EUR-BRL",
    "Bitcoin → Real": "BTC-BRL",
    "Libra → Real": "GBP-BRL"
}

# Cria uma caixa de seleção (dropdown) para o usuário escolher a moeda desejada
opcao = st.selectbox("Selecione a cotação:", list(moedas.keys()))

# Cria um botão que, ao ser clicado, executa a busca da cotação na API
if st.button("Buscar cotação"):
    # Monta a URL de consulta concatenando o endpoint da API com o código da moeda escolhida
    url = f"https://economia.awesomeapi.com.br/json/last/{moedas[opcao]}"

    # Envia a requisição GET para a API
    resposta = requests.get(url)

    # Verifica se a requisição foi bem sucedida (código HTTP 200)
    if resposta.status_code == 200:
        # Converte a resposta JSON para um dicionário Python
        dados = resposta.json()

        # A API retorna um dicionário com a chave sendo o código da moeda sem hífen (ex: "USDBRL")
        # Pega essa chave para acessar os dados da moeda
        chave = list(dados.keys())[0]  # exemplo: "USDBRL"
        info = dados[chave]            # Dados específicos da moeda selecionada

        # Exibe um subtítulo com o nome da moeda (ex: "Dólar Americano/Real Brasileiro")
        st.subheader(info["name"])

        # Mostra os dados da moeda formatados com negrito e texto explicativo
        st.write(f"**Alta do dia:** {info['high']}")
        st.write(f"**Baixa do dia:** {info['low']}")
        st.write(f"**Variação:** {info['varBid']}")
        st.write(f"**Cotação atual (compra):** R$ {info['bid']}")
        st.write(f"**Cotação atual (venda):** R$ {info['ask']}")
    else:
        # Caso haja erro na requisição, exibe uma mensagem de erro na interface
        st.error("Erro ao buscar a cotação.")
