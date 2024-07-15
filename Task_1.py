def total_salary(path):
    
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Розділяємо рядок на прізвище та зарплату
                    name, salary = line.strip().split(',')
                    # Додаємо зарплату до загальної суми
                    total += float(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}. Цей рядок буде пропущено.")

        if count == 0:
            print("Файл порожній або не містить коректних даних.")
            return 0, 0

        # Обчислюємо середню зарплату
        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0
    except Exception as e:
        print(f"Виникла неочікувана помилка: {e}")
        return 0, 0
