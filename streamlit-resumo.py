# import streamlit as st
# para importar streamlit se usa esse comando
# import streamlit as st
# pip install streamlit primeiro rode esse codigo no terminal para instalar o streamlit, ai voce coloca esse dps streamlit run app.py com 
# o nome do seu arquivo, depois vai pedir seu email. Ai sim vai aparecer o link, só colar no navegador e sua pagina web vai estar aberta
#como construir um site com streamlit
# conhecimentos básicos:
# st.title() → título grande

# st.write() → escreve texto ou mostra objetos

# st.text_input() → campo de texto

# st.button() → botão

# st.slider() → controle deslizante
# Permite que o usuário selecione um valor (ou intervalo de valores) deslizando um botão. Pode ser número inteiro, número decimal, data, etc.
# st.line_chart() → gráfico de linha
# Gera um gráfico de linha automaticamente a partir de dados numéricos (como listas, arrays ou DataFrames do Pandas).

# st.text_input("Seu nome:")
# st.number_input("Digite um número")
# st.slider("Escolha um valor", 0, 100)
# st.checkbox("Aceito os termos")
# st.radio("Escolha uma opção", ["A", "B", "C"])
# st.selectbox("Selecione", ["Python", "R", "Julia"])
# # st.file_uploader("Envie um arquivo")

# Por padrão, os links em Markdown no Streamlit já abrem em nova aba. Se quiser garantir isso, pode usar HTML dentro do Markdown:

# st.markdown('<a href="https://www.google.com" target="_blank">Abrir Google em nova aba</a>', unsafe_allow_html=True)


# ⚠️ Use unsafe_allow_html=True com cuidado, pois ele permite HTML puro no app.

# ✅ 3. Com botões simulando links (estilo UX)

# Se quiser um botão que parece um link:

# if st.button("Abrir Google"):#     st.markdown("[Clique aqui para visitar o Google](https://www.google.com)")


# Ou com um botão que abre automaticamente o link:

# import webbrowser

# if st.button("Abrir Google"):
#     webbrowser.open_new_tab("https://www.google.com")


# ⚠️ Isso só funciona localmente, não em apps hospedados online (como no Streamlit Cloud).

# ✅ 4. Na sidebar
# with st.sidebar:
#     st.markdown("[🔗 Link para o GitHub](https://github.com/seu-usuario)")

# 🧪 Exemplo completo com tudo:
# import streamlit as st

# st.title("Links no Streamlit")

# st.markdown("### 🔗 Link simples com Markdown")
# st.markdown("[Visite o Google](https://www.google.com)")

# st.markdown("### 🌐 Link que abre em nova aba (HTML)")
# st.markdown('<a href="https://www.google.com" target="_blank">Google (nova aba)</a>', unsafe_allow_html=True)

# st.markdown("### 🧭 Link na barra lateral")
# with st.sidebar:
#     st.markdown("[GitHub](https://github.com)", unsafe_allow_html=True)


# Se quiser, posso te ajudar a adicionar links no contexto de um app específico (ex: botão para baixar arquivo, abrir documentação, etc.). É só dizer!

# 🔍 O que é uma API?

# API significa Application Programming Interface (Interface de Programação de Aplicações).

# É um conjunto de regras que permite que diferentes softwares se comuniquem entre si.

# 🧱 Conceito básico:

# Pense em uma API como um "garçom" em um restaurante:

# Você (o cliente) faz um pedido.

# O garçom (API) leva o pedido para a cozinha (servidor).

# A cozinha prepara e devolve a resposta.

# O garçom (API) te entrega o prato (dados).

# 🧩 Para que serve uma API?

# 🔄 Conectar sistemas diferentes.

# 📦 Obter dados de outros serviços (ex: clima, mapas, pagamentos, redes sociais).

# 🤖 Integrar inteligência artificial, modelos de machine learning, etc.

# 📲 Criar apps que falam com servidores.

# 🔑 Componentes principais de uma API Web:
# Conceito	Explicação rápida
# Endpoint	URL específica que representa um recurso (ex: /usuarios, /produtos/1)
# Métodos HTTP	Forma da requisição (veja abaixo)
# Request	O pedido que o cliente envia
# Response	A resposta do servidor (geralmente em JSON)
# Status Code	Código indicando o resultado (ex: 200 = OK, 404 = Não encontrado)
# 📬 Métodos HTTP mais comuns:
# Método	Função	Exemplo
# GET	Ler dados	GET /usuarios
# POST	Criar dados	POST /usuarios
# PUT	Atualizar dados	PUT /usuarios/1
# DELETE	Apagar dados	DELETE /usuarios/1
# 📦 Exemplo de requisição:
# Requisição:
# GET https://api.exemplo.com/usuarios/1

# Resposta (JSON):
# {
#   "id": 1,
#   "nome": "João",
#   "email": "joao@email.com"
# }

# 🧠 Exemplos de APIs famosas:
# API	Para quê serve?
# OpenWeatherMap	Dados de clima
# Google Maps API	Mapas, rotas, geolocalização
# Twitter API	Ler ou postar tweets
# Stripe API	Pagamentos online
# OpenAI API	ChatGPT, geração de texto, imagem, etc.
# 🛠️ Ferramentas para testar APIs:

# Postman – Envia e testa requisições.

# curl – Testes via terminal.

# Insomnia – Outra opção parecida com o Postman.

# Browser – Você pode testar requisições GET direto na URL.

# ✅ Resumo rápido:

# API é uma ponte entre aplicações.

# Permite automação, integração e acesso a dados.

# Trabalha com requisições e respostas (geralmente em HTTP e JSON).

# Facilita a comunicação entre frontend ↔ backend, ou entre sistemas diferentes.

# Se quiser, posso te mostrar como criar uma API simples em Python com Flask ou FastAPI, ou como consumir uma API com requests. Quer seguir por esse caminho?

# Você disse:
# JSON, CONCEITOS E INSTALAÇÃO
# O ChatGPT disse:

# Perfeito! Vamos direto ao ponto com os conceitos básicos sobre JSON, seguido de como usar (não instalar) JSON em Python, já que ele já vem incluso no Python — não precisa instalar nada.

# 🧾 O que é JSON?

# JSON significa JavaScript Object Notation.
# É um formato leve de troca de dados usado para transmitir informações entre sistemas, especialmente na web.

# 🔍 Conceito Básico:

# JSON é uma estrutura de texto que representa dados organizados em pares chave:valor.

# Muito parecido com dicionários do Python.

# Usado em APIs, configurações, comunicação entre sistemas, etc.

# 🧱 Estrutura JSON (Exemplo):
# {
#   "nome": "Maria",
#   "idade": 30,
#   "tem_carteira": true,
#   "filhos": ["Ana", "Lucas"]
# }


# {} → objeto (dicionário)

# [] → lista

# true/false → booleano

# Strings entre aspas duplas (" ")

# 🐍 Como usar JSON no Python

# O Python já vem com o módulo json embutido.
# Você não precisa instalar — basta importar.

# ✅ Importar:
# import json

# 🔄 Conversões básicas:
# 1. 📦 De Python → JSON (serializar):
# import json

# dados = {"nome": "Maria", "idade": 30}
# # json_string = json.dumps(dados)

# # print(json_string)


# # 🔁 Resultado:

# # {"nome": "Maria", "idade": 30}

# # 2. 📥 De JSON → Python (desserializar):
# # import json

# # json_string = '{"nome": "Maria", "idade": 30}'
# # dados = json.loads(json_string)

# # print(dados["nome"])  # Maria

# # 📁 Ler e escrever JSON em arquivos
# # ➤ Salvar em um arquivo .json:
# # import json

# # dados = {"nome": "João", "idade": 25}

# # with open("dados.json", "w") as f:
# #     json.dump(dados, f)

# # ➤ Ler de um arquivo .json:
# # import json

# # with open("dados.json", "r") as f:
# #     dados = json.load(f)

# # print(dados)

# # ✅ Quando usar JSON?

# # Ao consumir ou enviar dados via APIs

# # Para salvar configurações de apps

# # Para armazenar dados simples

# # Em aplicações web, mobile, e microserviços

# # 🧪 Resumo:
# # Conceito	JSON
# # Tipo	Formato de texto
# # Usado para	Troca de dados
# # Baseado em	Chave e valor
# # Suporte em Python	Módulo json embutido
# # Instalação	❌ Não precisa instalar

# # Se quiser, posso te mostrar como usar JSON em um projeto com Streamlit, API ou com consumo de dados da web. Só dizer o que você está estudando ou desenvolvendo.

# import streamlit as st            # Importa o Streamlit para criar a interface web
# import requests                  # Importa requests para fazer requisições HTTP

# # Define o título da aplicação que será mostrado no topo da página
# st.title("Cotação de Moedas - AwesomeAPI")

# # Dicionário com as opções de moedas disponíveis para consulta
# # A chave é o texto exibido para o usuário, o valor é o código usado na API
# moedas = {
#     "Dólar → Real": "USD-BRL",
#     "Euro → Real": "EUR-BRL",
#     "Bitcoin → Real": "BTC-BRL",
#     "Libra → Real": "GBP-BRL"
# }

# # Cria uma caixa de seleção (dropdown) para o usuário escolher a moeda desejada
# opcao = st.selectbox("Selecione a cotação:", list(moedas.keys()))

# # Cria um botão que, ao ser clicado, executa a busca da cotação na API
# if st.button("Buscar cotação"):
#     # Monta a URL de consulta concatenando o endpoint da API com o código da moeda escolhida
#     url = f"https://economia.awesomeapi.com.br/json/last/{moedas[opcao]}"

#     # Envia a requisição GET para a API
#     resposta = requests.get(url)

#     # Verifica se a requisição foi bem sucedida (código HTTP 200)
#     if resposta.status_code == 200:
#         # Converte a resposta JSON para um dicionário Python
#         dados = resposta.json()

#         # A API retorna um dicionário com a chave sendo o código da moeda sem hífen (ex: "USDBRL")
#         # Pega essa chave para acessar os dados da moeda
#         chave = list(dados.keys())[0]  # exemplo: "USDBRL"
#         info = dados[chave]            # Dados específicos da moeda selecionada

#         # Exibe um subtítulo com o nome da moeda (ex: "Dólar Americano/Real Brasileiro")
#         st.subheader(info["name"])

#         # Mostra os dados da moeda formatados com negrito e texto explicativo
#         st.write(f"**Alta do dia:** {info['high']}")
#         st.write(f"**Baixa do dia:** {info['low']}")
#         st.write(f"**Variação:** {info['varBid']}")
#         st.write(f"**Cotação atual (compra):** R$ {info['bid']}")
#         st.write(f"**Cotação atual (venda):** R$ {info['ask']}")
#     else:
#         # Caso haja erro na requisição, exibe uma mensagem de erro na interface
#         st.error("Erro ao buscar a cotação.")



# git config --global user.name "Seu Nome" 
# git config --global user.email "seu.email@exemplo.com"

# git config --global --list

# 