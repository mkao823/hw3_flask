from flask import Flask
from flask import render_template

myapp_obj = Flask(__name__)

@myapp_obj.route('/')
def home():
    name = 'Lisa'
    city_names = ['city']
    return f'''
    <html>
    <head>
        <h1>Welcome {name}!</h1>
    </head>
    <body>
        <p>
            <a href="https://www.google.com/">not google</a>
        </p>    
            <p1>
                for city in city_names
                    print(city)
            </p1>
    </body>
    </html>
    '''

