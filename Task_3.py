import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init()

def print_directory_structure(directory, prefix=""):
    
    # Отримуємо список всіх елементів в директорії
    try:
        contents = list(directory.iterdir())
    except PermissionError:
        print(f"{prefix}{Fore.RED}Помилка доступу: {directory}{Style.RESET_ALL}")
        return

    # Сортуємо: спочатку директорії, потім файли
    contents.sort(key=lambda x: (not x.is_dir(), x.name.lower()))

    for item in contents:
        if item.is_dir():
            # Виводимо ім'я директорії синім кольором
            print(f"{prefix}{Fore.BLUE} {item.name}{Style.RESET_ALL}")
            # Рекурсивний виклик для підпапки
            print_directory_structure(item, prefix + "  ")
        else:
            # Виводимо ім'я файлу зеленим кольором
            print(f"{prefix}{Fore.GREEN} {item.name}{Style.RESET_ALL}")

def main():
    # Перевіряємо, чи передано аргумент командного рядка
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python {sys.argv[0]} <шлях_до_директорії>{Style.RESET_ALL}")
        sys.exit(1)

    # Отримуємо шлях до директорії з аргументу командного рядка
    directory_path = Path(sys.argv[1])

    # Перевіряємо, чи існує директорія
    if not directory_path.exists():
        print(f"{Fore.RED}Помилка: Директорія '{directory_path}' не існує.{Style.RESET_ALL}")
        sys.exit(1)

    # Перевіряємо, чи це дійсно директорія
    if not directory_path.is_dir():
        print(f"{Fore.RED}Помилка: '{directory_path}' не є директорією.{Style.RESET_ALL}")
        sys.exit(1)

    # Виводимо структуру директорії
    print(f"{Fore.YELLOW}Структура директорії '{directory_path}':{Style.RESET_ALL}")
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()