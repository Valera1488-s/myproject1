from flask import Flask

app = Flask(name)

@app.route('/')
def hello():
    return "Hello, World!"

if__name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
