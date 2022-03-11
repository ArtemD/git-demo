from flask import Flask

# Create the application object
app = Flask(__name__)

@app.route('/')
def index():
    """ Main page """
    return 'Web App with Python Flask!'

@app.route('/api/v1/hello')
def hello():
    """ Hello World page """
    return 'Hello World!'

# Run the application in debug mode
app.run(host='0.0.0.0', port=8000)