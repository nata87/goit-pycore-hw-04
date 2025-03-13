def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                try:
                    _, salary = line.strip().split(",")
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Помилка у форматі рядка: {line.strip()}")
        
        if not salaries:
            return 0, 0  
        
        total = sum(salaries)
        average = total // len(salaries) 
        return total, average
    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0
    
    except Exception as exception:
        print(f"Сталася помилка: {exception}")
        return 0, 0

total, average = total_salary("task1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
