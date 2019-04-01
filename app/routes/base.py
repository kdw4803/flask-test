def init_app(app):
    @app.route("/")
    def index():
        return "Index!!"

    @app.route("/hello")
    def hello():
        return "Hello World!"