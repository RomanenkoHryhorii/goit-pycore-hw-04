def get_cats_info(path):
  
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Розділяємо рядок на id, ім'я та вік
                    cat_id, name, age = line.strip().split(',')
                    # Створюємо словник з інформацією про кота
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info.append(cat_info)
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}. Цей рядок буде пропущено.")

        if not cats_info:
            print("Файл порожній або не містить коректних даних.")

        return cats_info

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []
    except Exception as e:
        print(f"Виникла неочікувана помилка: {e}")
        return []

