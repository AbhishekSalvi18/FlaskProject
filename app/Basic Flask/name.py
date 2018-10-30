from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello World'


@app.route('/hi/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/hi/<int:age>')
def age(age):
    return 'age= %d' % age

if __name__ == '__main__':
    app.run(debug = True)
