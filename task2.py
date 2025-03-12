def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:  
                    cat_id, name, age = parts
                    cats_list.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
         return None
    except Exception as exception:
        print(f"Помилка при читанні файлу: {exception}")
    
    return cats_list


print(get_cats_info("task2/cats_file.txt"))
