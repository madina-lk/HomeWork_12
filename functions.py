import json

POST_PATH = "posts.json"


def get_all_posts(path):
    """Метод выгружает данные из файла .json"""

    file = open(path, encoding="utf-8")                     # открытие json - файла
    data = json.load(file)                                  # загрузка списка словарей из json - файла

    return data                                             # возвращаем список словарей


def search_post(sbstr):
    """Поиск подстроки sbstr в строке поля content списка словарей json-файла"""

    sbstr_lower = sbstr.lower()                             # приведение к нижнему регистру
    post_found = []                                         # объявление пустого списка для последующего заполнения
    posts = get_all_posts(POST_PATH)                        # получение списка словарей из json-файла

    for post in posts:
        if sbstr_lower in post["content"].lower():          # поиск подстроки в строках поля контента
            post_found.append(post)                         # добавление нового словаря к списку словарей

    return post_found


def load_new_record(path, content):
    """
        В методе происходит добавление нового словаря в список словарей,
        затем перезапись существующего json-файла с новыми данными
    """

    posts = get_all_posts(POST_PATH)                        # получение списка словарей из json-файла
    new_record = {"pic": path, "content": content}          # формирование нового словаря
    posts.append(new_record)                                # добавление словаря к списку словарей

    with open(POST_PATH, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)   # перезапись файла

    return posts
