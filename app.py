from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! This is a flask application'
    
    
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')