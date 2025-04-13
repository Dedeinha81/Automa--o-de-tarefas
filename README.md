Este projeto automatiza o processo de cadastro de produtos em um sistema web utilizando Python e a
biblioteca pyautogui. Ele simula ações humanas como abrir o navegador, preencher formulários e interagir
com a interface gráfica.

 Etapas do código
 
1. Importação de biblioteca

import pyautogui

import time

import pandas

pyautogui: usada para simular ações do mouse e teclado.

time: usada para pausar o código por alguns segundos.

pandas: usada para ler o arquivo .csv com os dados dos produtos.

2. Configuração da pausa entre comandos

pyautogui.PAUSE = 0.5
Isso define um tempo de espera de 0.5 segundos entre cada comando do pyautogui, para não executar muito rápido.

3. Abrir o navegador e acessar o sistema da empresa
   
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

Aqui, o código:

Abre o menu Iniciar do Windows

Digita “chrome”

Acessa a URL do sistema

Aguarda o carregamento da página

4. Fazer login no sistema

pyautogui.click(x=854, y=313)
pyautogui.write("dedeinha81@hotmail.com")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
Simula um clique no campo de e-mail e faz o login com o e-mail informado.

5. Ler a planilha de produtos

tabela = pandas.read_csv("produtos.csv")
print(tabela)
Lê o arquivo produtos.csv, que contém os dados a serem cadastrados, e exibe no terminal.

6. Cadastrar os produtos um por um

for linha in tabela.index:
    
Para cada linha da planilha, o código:

Clica no botão de “Novo Produto”

Preenche os campos: código, marca, tipo, categoria, preço unitário, custo, observações

Pressiona Enter para enviar

Dá scroll na página para garantir que o botão continue visível

