from flask import Flask
from application.mainfolder.views import Views


def server():

    app = Flask(__name__)
    Views.get_views(app)
    return app


App = server()


if __name__ == '__main__':
    App.run(debug=True, port=1234)
