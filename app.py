from flask import Flask

app = Flask(__name__)

# The General GET command processing
@app.route('/', methods = ['GET'])
def index():
    return("\n=====================\nWelcome to BRTGPT\nCONGRATULATIONS you have SUCCESSFULLY CONNECTED\n=====================\n\n")


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
