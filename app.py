from flask import Flask

app = Flask(name)

@app.route('/')
def hello():
    return "Hello, World!"

if__nam__e == '__main__':
    app.run(host='0.0.0.0', port=80)
