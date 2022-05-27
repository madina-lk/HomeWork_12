import logging                                                      # импорт модуля логирования

from flask import Blueprint, render_template, request               # импорт класса блюпринт
from functions import *

main_blueprint = Blueprint('main_blueprint', __name__)              # создание нового блюпринта с заданным именм
logging.basicConfig(filename='log_file.log', level=logging.INFO)


@main_blueprint.route('/')                                          # создание вьюшки для главной страницы
def main_page():
    """Вьюшка для главной страницы"""
    return render_template('index.html')                            # обращение к шаблону


@main_blueprint.route('/search', methods=['GET'])                   # создание вьюшки для страницы поиска
def search_page():
    """Поиск поста"""

    s = request.args.get('s', "")                                   # получение доступа к параметрам адресной строки

    try:
        result_posts = search_post(s)                               # поиск
        return render_template('post_list.html', s=s, result=result_posts)
    except FileNotFoundError:                                       # обработка ошибки
        logging.error("Нет доступа к данным")                        # запись в лог
        return "Нет доступа к данным"


