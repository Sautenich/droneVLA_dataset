import os
import json
import random

def create_dataset(folder_path, output_file):
    images = [img for img in os.listdir(folder_path) if img.lower().endswith(('png', 'jpg', 'jpeg'))]
    dataset = []
    
    for img in images:
        name = os.path.splitext(img)[0]  # Извлекаем имя знаменитости без расширения
        prompt = f"Fly through the gate with {name}"
        
        # Выбираем два случайных имени, которые не совпадают с текущим
        choices = [img] + random.sample([i for i in images if i != img], 2)
        random.shuffle(choices)
        correct_index = choices.index(img) + 1  # Индексация с 1
        
        dataset.append({
            "prompt": prompt,
            "options": choices,
            "correct": correct_index
        })
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    create_dataset("images", "hr_celeb_dataset.json")
