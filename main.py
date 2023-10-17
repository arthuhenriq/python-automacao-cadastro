import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(4)

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=901, y=451)
# escrever o seu email
pyautogui.write("arthuhenriq@gmail.com")
pyautogui.press("tab")  # passando pro próximo campo
pyautogui.write("7342Artyh*!")
pyautogui.click(x=979, y=656)  # clique no botao de login
time.sleep(3)

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Cadastrar um produto

for linha in tabela.index:
    # clicar no campo de inserir a marca do produto
    pyautogui.click(x=853, y=310)

    # pegar da tabela o valor do campo que a gente quer preencher
    # preencher o campo
    # passar para o proximo campo
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    pyautogui.press("enter")  # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
