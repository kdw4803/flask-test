def init_app(app):
    @app.route("/")
    def index():
        return app.config['ENV']

    @app.route("/hello")
    def hello():
        return "Hello World!"