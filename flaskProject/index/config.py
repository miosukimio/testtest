import os

current_dir = os.path.dirname(__file__)
absolute_path = os.path.abspath(current_dir)
root_dir = os.path.dirname(absolute_path)
media_root = os.path.join(root_dir, 'static/media')
video_dir=os.path.join(media_root,'video')
sounds_dir=os.path.join(media_root,'sounds')

USERNAME = 'root' #设置登录账号
PASSWORD = '123456' #设置登录密码
HOST = '127.0.0.1' #设置主机地址
PORT = '3306' #设置端口号
DATABASE ='flask_web' #设置访问的数据库

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
