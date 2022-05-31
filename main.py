from app import app
from app import view


if __name__ == '__main__':
    app.debug = True
    app.run(port=8083)
