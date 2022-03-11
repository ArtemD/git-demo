from flask import Flask

# Create the application object
app = Flask(__name__)

# this is in master

@app.route('/')
def index():
    """ Main page """
    return 'Web App with Python Flask!'

# This is a test comment

@app.route('/api/v1/hello')
def hello():
    """ Hello World page """
    return 'Hello World!'

# Run the application in debug mode
app.run(host='0.0.0.0', port=8000)