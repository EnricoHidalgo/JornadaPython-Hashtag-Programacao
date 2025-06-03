import pyautogui
# pyautogui.click = clicar
# pyautogui.press = apertar uma tecla
# pyautogui.write = escrever um texto
# pyautogui.hotkey = apertar um atalho do teclado

import time
# time.sleep = pausa em lugar específico

import pandas

tabela = pandas.read_csv("produtos.csv")

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('brave')
pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
pyautogui.press('tab')

time.sleep(3)

pyautogui.click(x=801, y=367);
pyautogui.write('testeHashtag@gmail.com')
pyautogui.click(x=711, y=469);
pyautogui.write('senha1234')
pyautogui.click(x=953, y=525);

time.sleep(3)
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=813, y=251)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, "categoria"]) 
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press('tab')
    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(1000)  





