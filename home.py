from flask import Flask
from flask import render_template

myapp_obj = Flask(__name__)

@myapp_obj.route('/')
def home():
    name = 'username'
    city_names = ['city']
    return f'''
    <html>
    <h1>Welcome {name}</h1>
        <h2>
            <a href="https://www.google.com/">not google</a>
        </h2>    

    </html>
    '''

myapp_obj.run()