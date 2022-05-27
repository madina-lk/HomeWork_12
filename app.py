from flask import Flask

from main.main import main_blueprint                # Импортируем блюпринты из их пакетов
from loader.loader import loader_blueprint

app = Flask(__name__)


app.register_blueprint(main_blueprint)              # Регистрируем блюпринт main_blueprint
app.register_blueprint(loader_blueprint)            # Регистрируем блюпринт loader_blueprint


if __name__ == '__main__':
    app.run()
