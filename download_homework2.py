import requests

# URL файла
url = "https://gbcdn.mrgcdn.ru/uploads/asset/5963564/attachment/8bf75400e9969514883649204e99f17d.ipynb"

# Скачивание файла
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Сохранение файла
    with open("downloaded_file2.ipynb", "wb") as file:
        file.write(response.content)
    print("Файл успешно скачан и сохранен как 'downloaded_file.ipynb'.")
else:
    print("Ошибка при скачивании файла:", response.status_code)