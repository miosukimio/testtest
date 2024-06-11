from flask import Flask,request,session
from flask_sqlalchemy import SQLAlchemy

# 初始化一个SQLAlchemy对象
db = SQLAlchemy()


from index import config,admin
from flask_babelex import Babel



app = Flask(__name__,template_folder='../templates',static_folder='../static',static_url_path='/static')

app.debug=True
app.config['SQLALCHEMY_DATABASE_URI']=config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO']=False
app.config['SECRET_KEY']='jsbdhkjsbdjsklds'


# 初始化数据库
with app.app_context():
    db.app=app
    db.init_app(app)
    admin.register_admin(app)
    babel = Babel(app)
    #db.drop_all() # 清库
    #db.create_all() # 创建库

@babel.localeselector
def get_locale(): #管理页面切换语言至中文
    override = request.args.get('lang')

    if override:
        session['lang'] = override

    return session.get('lang', 'zh_Hans_CN')



