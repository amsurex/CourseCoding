import requests

# Вводим API токен
access_token = input("Введите ваш API токен: ")

# Получаем информацию о профиле

url = f"https://graph.instagram.com/me?fields=id,username&access_token={access_token}" 
response = requests.get(url)
data = response.json()

if "error" in data:
    print("Произошла ошибка:", data["error"]["message"])
else:
    user_id = data["id"]
    username = data["username"]
    print("Информация о профиле:")
    print("ID: ", user_id)
    print("Имя пользователя: ", username)

# Получаем информацию о публикациях профиля

url = f"https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,thumbnail_url&access_token={access_token}"
response = requests.get(url)
data = response.json()

if "error" in data:
    print("Произошла ошибка:", data["error"]["message"])
else:
    if "data" in data:
        print("Публикации пользователя:")
        for post in data["data"]:
            post_id = post["id"]
            media_type = post["media_type"]
            media_url = post["media_url"]
            print("ID публикации:", post_id)
            print("Тип медиа:", media_type)
            print("URL медиа:", media_url)
            print("-" * 10)
        else:
            print("На этом все.")