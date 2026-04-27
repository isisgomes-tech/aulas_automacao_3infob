import pyautogui

#Opção 1:
#Localiza uma imagem na tela e retorna uma caixa, com coordenada X e Y do ponto inicial da caixa left+top e largura e altura da caixa.
box = pyautogui.locateOnScreen('aula6\\8.png')
#Com a caixa encontrada, a função center retorna a coordenada xy do centro da caixa "imagem".
centro_box = pyautogui.center(box)
print(centro_box)

#Opção 2:

xy2 = pyautogui.locateCenterOnScreen('aula6\\8.png', confidence=0.95)
print(xy2)

xy3 = pyautogui.locateCenterOnScreen('aula6\\bolavermelha.png', confidence=0.5)
print(xy3)