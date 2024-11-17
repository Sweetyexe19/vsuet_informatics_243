import requests
import json
import tkinter as tk
from tkinter import messagebox

# Функция для получения информации о репозитории
def get_repo_info(repo_name):
    url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(url)

    if response.status_code == 200:
        repo_data = response.json()
        repo_info = {
            'company': None,
            'created at': repo_data.get('created_at'),
            'email': None,
            'id': repo_data.get('id'),
            'name': repo_data.get('name'),
            'url': repo_data.get('html_url')  # Изменение на 'html_url' для получения URL репозитория
        }
        return repo_info
    else:
        messagebox.showerror("Ошибка", "Репозиторий не найден. Проверьте имя репозитория.")

# Функция для обработки нажатия кнопки
def on_button_click():
    repo_name = entry.get()
    if repo_name:
        repo_info = get_repo_info(repo_name)
        if repo_info:
            with open(f"{repo_name}_info.json", "w") as json_file:
                json.dump(repo_info, json_file, indent=4)
            messagebox.showinfo("Успех", f"Информация о репозитории сохранена в файл '{repo_name}_info.json'")
    else:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите имя репозитория.")

# Настройка графического интерфейса
root = tk.Tk()
root.title("GitHub Repo Info Fetcher")

tk.Label(root, text="Введите имя репозитория:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Получить информацию", command=on_button_click)
button.pack(pady=20)

root.mainloop()