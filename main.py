import pyautogui
import keyboard

### site: "https://offline-dino-game.firebaseapp.com/" ###

game_is_on = True

while game_is_on:
    screen = pyautogui.screenshot()
    bg_color = screen.getpixel((70,190))

    x = screen.getpixel((500,910))
    x2 = screen.getpixel((510,910))
    x3 = screen.getpixel((520,910))
    x4 = screen.getpixel((530,910))
    x5 = screen.getpixel((540,910))
    y = screen.getpixel((500,800))
    y2 = screen.getpixel((510,800))
    y3 = screen.getpixel((520,800))
    y4 = screen.getpixel((530,800))
    y5 = screen.getpixel((540,800))

    if bg_color != x or bg_color != x2 or bg_color != x3 or bg_color != x4 or bg_color != x5 or bg_color != y or bg_color != y2 or bg_color != y3 or bg_color != y4 or bg_color != y5:
        keyboard.press("space")

    if keyboard.is_pressed("s"):
        game_is_on = False


      