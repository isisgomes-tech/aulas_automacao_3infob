import pyautogui

xy3 = pyautogui.locateCenterOnScreen('aula6\\bolavermelha.png', confidence=0.85, grayscale=False)
print(xy3)

pyautogui.click(xy3, duration=1)