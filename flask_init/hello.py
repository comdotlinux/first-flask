import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World From Flask!!!!! :D'

@app.route('/users/<username>')
def say_hi_to_user(username):
    return 'Hey there.... %s' % username

@app.route('/user/<int:userid>')
def get_user_by_id(userid):
    return 'user id entered %d' % userid
    
    
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)

