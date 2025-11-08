import os
import time
import sys


# Определение цветовых констант
class Colors:
    BLUE = "\033[01;38;05;45m"
    WHITE = "\033[38;05;15m"
    ORANGE = "\033[38;05;202m"
    RESET = "\033[0m"
    MAGENTA = "\033[38;05;206m"
    GREEN = "\033[38;05;46m"
    RED = "\033[38;05;196m"
    AQUA = "\033[38;05;49m"
    YELLOW = "\033[33m"
    RAINBOW = [
    "#ff0000",
    "#ff5e00",
    "#ffea00",
    "#2bff00",
    "#00b3ff",
    "#0008ff",
    "#9900ff",
    ],
    MAIN = "\033[38;05;216m"
    TITLEST = "\033[38;05;222m"
    GRAY = "\033[38;05;240m"


# Проверка наличия библиотеки colorama
required_libraries = ['colorama', 'progress', 'maxgradient', 'rich']
missing_libraries = []

for lib in required_libraries:
    try:
        __import__(lib)
    except ImportError:
        missing_libraries.append(lib)
        

if missing_libraries:
    os.system("cls")
    print()
    print(Colors.WHITE + Colors.RED + "ERROR: Библиотека(и) " + Colors.GREEN + ", ".join(missing_libraries) + Colors.RED + " не установлена(ы). Выполнение кода невозможно." + Colors.RESET)
    print(Colors.BLUE + f"\nУстановите библиотеку(и): {', '.join(missing_libraries)} с помощью:")
    print(f"pip install {', '.join(missing_libraries)}")
    print(Colors.RESET)
    sys.exit(1)
else:
    import colorama
    import progress
    from rich.console import Console
    from maxgradient import Gradient

colorama.init()

class CommandBar:
    def __init__(self):
        self.console = Console()
        self.title = Gradient("CommandBar", colors=Colors.RAINBOW) + " by Nikitich1423"
        self.version = Colors.MAGENTA + "v." + Colors.GREEN + "1.1.1\n" + Colors.RESET + f"\nОбновление:\n- Радужный градиент для {Gradient("CommandBar", colors=Colors.RAINBOW)}"
        self.error_message = Colors.RED + "Invalid command." + Colors.RESET
        self.debug_mode = Colors.YELLOW + "Debug mode activated." + Colors.RESET

    def display_start_text(self):
        os.system("cls")
        self.delay_print(self.title + "\n" + self.version, delay=0.05)
        print()

    def delay_print(self, text: str, delay=0.1):
        for char in text:
            command_bar = CommandBar()

            command_bar.console.print(char, end='')
            time.sleep(delay)
        print()
       
    def start_text(self):
        os.system("cls")
        command_bar = CommandBar()
        command_bar.console.print(self.title + "\n" + self.version + "\n")

    def input_check(self, user_input):      
        if user_input == "process.execute <...>":
            return True
        else:
            return False

    def process_execute_action(self, user_input):
        if user_input.lower() == 'process.execute <...>':
            os.system("cls")
            self.start_text()  # Используем метод экземпляра
            command_input = input(Colors.MAGENTA + "process.execute <...>:" + Colors.GREEN + " ")
            if command_input.lower() == "exit":
                os.system("cls")
                print(Colors.RESET)
                time.sleep(0.5)
                print(self.debug_mode)  # Используем атрибут экземпляра
                time.sleep(0.5)
                print(f"{colorama.Fore.YELLOW}{colorama.Style.BRIGHT}DEBUG:{colorama.Style.NORMAL} {colorama.Fore.WHITE}event 'exit' fetched")    
                time.sleep(0.5)            
                print(f"{colorama.Fore.YELLOW}{colorama.Style.BRIGHT}DEBUG:{colorama.Style.NORMAL} {colorama.Fore.WHITE}exit code complete.{colorama.Style.RESET_ALL}")
                print()
                time.sleep(0.5)
                sys.exit()
            else:
                os.system("cls")
                print()
                print(f"{colorama.Fore.RED}{colorama.Style.BRIGHT}ERROR:{colorama.Style.NORMAL} {colorama.Fore.WHITE}{self.error_message}")  # Используем атрибут экземпляра
                print(f"{colorama.Fore.LIGHTBLUE_EX}{colorama.Style.BRIGHT}ACTION:{colorama.Style.NORMAL} {colorama.Fore.WHITE}Close.{colorama.Style.RESET_ALL}")
                print()
                sys.exit()

    def exit_text(self):
        os.system("cls")
        print()
        print("\033[01;38;05;220m> Ctrl + C <" + Colors.RESET)
        print("\033[38;05;196mПрограмма закрыта" + Colors.RESET)
        print()
        sys.exit()
        
def start() -> CommandBar:
    """Запустить `CommandBar`"""
    command_bar = CommandBar()
    command_bar.display_start_text()
    
    while True:
        try:
            user_input = input()
            if command_bar.input_check(user_input):
                command_bar.process_execute_action(user_input)
            else:
                os.system("cls")
                command_bar.start_text()

        except KeyboardInterrupt:
            command_bar.exit_text()








def delay_print(text: str, delay=0.1):
    """
    Фукнция
    ---
    Функция, пишущая текст с задержкой
    \n
    `text`: Текст (`str`)
    \n
    `delay`:
    Задержка написания (По умолчанию `0.1`)
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

    print()

def delayed_print(delay=0.1):
    """
    Декоратор
    ---
    Функция, пишущая текст с задержкой
    \n
    `delay`:
    Задержка написания (По умолчанию `0.1`)
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for char in result:
                print(char, end='', flush=True)
                time.sleep(delay)
            print()
        return wrapper
    return decorator