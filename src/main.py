from application import Application

app = Application()

if __name__ == '__main__':
    """
    if running app using development flask server
    ../src$ python main.py
    """
    app.run()

if __name__ != '__main__':
    """
    if running app from Gunicorn WSGI production server
    ../src$ gunicorn wsgi:app --bind 0.0.0.0:5000 -w 4
    """
    app = app.app
