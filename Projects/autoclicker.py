import pyautogui
from pynput.keyboard import *
import os
from doc import Colors



#  ======== настройки ========
delay = 0.000000000000000000000000000000000000000001
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
#  ==========================

os.system("cls")
pause = True
running = True
titlest = Colors.TITLEST
gray = Colors.GRAY
reset = Colors.RESET

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print(Colors.GREEN + "[Запущено]" + Colors.RESET)
    elif key == pause_key:
        pause = True
        print(Colors.ORANGE + "[Пауза]" + Colors.RESET)
    elif key == exit_key:
        running = False
        print(Colors.RED + "[Выход]" + Colors.RESET)



def display_controls():
    print(Colors.GRAY + "// " + Colors.MAIN + "Консольный автокликер от Nikitich1423" + Colors.RESET)
    print(Colors.GRAY +"// - " + Colors.TITLEST + "Настройки: " + Colors.RESET)
    print(Colors.ORANGE + "\t delay = " + str(delay) + ' sec' + '\n' + Colors.RESET)
    print(Colors.GRAY + "// - " + Colors.TITLEST + "Управление:" + Colors.RESET)
    print(Colors.GREEN + "\t F1" + Colors.RESET +" = Начать" )
    print(Colors.GREEN + "\t F2" + Colors.RESET +" = Пауза")
    print(Colors.GREEN + "\t ESC" + Colors.RESET +" = Выход")
    print(Colors.GRAY + "-----------------------------------------------------" + Colors.RESET)
    print("\033[03;38;05;15m" + 'Нажмите F1, чтобы запустить...' + Colors.RESET)


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()