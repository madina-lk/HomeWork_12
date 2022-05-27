import logging                                                                 # импорт модуля логирования
from flask import Blueprint, render_template, request, send_from_directory     # импорт класса блюпринт
from functions import *

UPLOAD_FOLDER = "./uploads/images"

loader_blueprint = Blueprint('loader_blueprint', __name__)                      # создание нового блюпринта с заданным именм
logging.basicConfig(filename='log_file.log', level=logging.INFO)                # добавление файла, в который пишутся логи


@loader_blueprint.route('/post', methods=['GET'])
def main_loader_page():
    """Вывод страницы добавления поста"""

    return render_template('post_form.html')                                    # обращение к шаблону


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    """Вьюшка для того, чтобы сделать содержимое папки доступным для HTTP-запросов с клиента"""

    return send_from_directory("uploads", path)                                 # передача клиенту запрошенного файла


@loader_blueprint.route('/post', methods=["POST"])
def page_upload():
    """Добавление нового поста"""

    picture = request.files.get("picture")                                      # получение объекта картинки из формы
    content = request.form.get('content')                                       # получение контента

    if not picture or not content:
        logging.info("Данные не внесены")
        return "Данные не внесены"
    try:                                                                        # обработка исключений
        filename = picture.filename                                             # получение имени файла у загруженного файла
        picture_url = UPLOAD_FOLDER + filename
        picture.save(picture_url)                                               # сохранение картинки под родным именем в папку uploaDS
    except TypeError:                                                           # обработка ошибки несоответствия типа
        logging.info("Неверный тип")                                            # запись в лог
        return "Неверный тип"
    except FileNotFoundError:                                                   # обработка ошибки отсутствия файла
        logging.info("Файл не найден")                                          # запись в лог
        return "Файл не найден"

    posts = load_new_record(picture_url, content)

    return render_template('post_uploaded.html', img=picture_url, content=content)
