from flask  import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c99d2943ab28da8b956686f2dfc53531'
from Main import routes