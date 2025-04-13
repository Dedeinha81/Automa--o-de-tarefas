import pyautogui
import time
 
#pyautogui.press -> apertar uma tecla
#pyautogui.write -> escrever um texto
#pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# digitar site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# esperar 3 segundos
time.sleep(3)

# Passo 2: Fazer login
# preencher email
pyautogui.click(x=854, y=313)
pyautogui.write("dedeinha81@hotmail.com")

#botao logar
pyautogui.press("tab")
pyautogui.press("enter")

# esperar 3 segundos
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar o produto
for linha in tabela.index: # para cada linha da minha tabela
    pyautogui.click(x=1103, y=219)

    codigo = str (tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    pyautogui.press("tab") # passar para o proximo campo
    marca = str (tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    pyautogui.press("tab") # passar para o proximo campo
    tipo = str (tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    pyautogui.press("tab") # passar para o proximo campo
    categoria = str (tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)MOLO000251    Logitech    Mouse   1   25.95   6.5     


    pyautogui.press("tab") # passar para o proximo campo
    preco_unitario = str (tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") # passar para o proximo campo
    custo = str (tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab") # passar para o proximo campo
    obs = str (tabela.loc[linha, "obs"])

    if obs != "nan":
     pyautogui.write(obs)

    pyautogui.press("tab") # passou para o botao enviar
    pyautogui.press("enter")

    pyautogui.scroll(10000)


