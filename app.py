from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yewq123221'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

# Temporary user loader
@login_manager.user_loader
def load_user(user_id):
    return None

from routes.auth import auth
from routes.dashboard import dashboard
from routes.upload import upload
from routes.analysis import analysis

app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(upload)
app.register_blueprint(analysis)

if __name__ == "__main__":
    app.run(debug=True)