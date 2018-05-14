from flask import Flask

app = Flask(__name__, instance_relative_config=True)
# app.config.from_object('config.default')


@app.route("/hello")
def hello_world():
    return "Hello, World!"


@app.route('/')
def index():
    return 'Index Page'


if __name__ == '__main__':
    app.run(debug=True)
