import datetime
from index import db


# 用户
class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, unique=True,primary_key=True,autoincrement=True,)
    username=db.Column(db.String(50),nullable = False)
    password=db.Column(db.String(50),nullable=False)
    phone=db.Column(db.String(20))
    email=db.Column(db.String(50))
    hiragana_dic=db.Column(db.String(255),nullable=True) # 五十音进度
    hiragana_time=db.Column(db.DateTime)
    last_video=db.Column(db.String(100),nullable=True) # 最后观看的视频
    video_time=db.Column(db.DateTime)
    score_dic=db.Column(db.String(255),nullable=True) # 练习题得分
    is_admin=db.Column(db.Boolean,default=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def get_hiragana_dic(self):
        if self.hiragana_dic:
            dic=eval(self.hiragana_dic)
        else:
            dic={}
        return dic

    def get_score_dic(self):
        if self.score_dic:
            dic=eval(self.score_dic)
        else:
            dic={}
        return dic




class HiraganaCategory(db.Model):
    __tablename__='h_category'
    id = db.Column(db.Integer, primary_key=True,unique=True, autoincrement=True)
    name=db.Column(db.String(50),nullable=True)
    hiragana = db.relationship('Hiragana', backref='hiragana', lazy=True)  # 一对多关系

    def to_dic(self):
        dic = {
            'id': self.id,
            'name': self.name,
        }
        return dic

class Hiragana(db.Model):
    __tablename__='hiragana'
    id=db.Column(db.Integer, primary_key = True, autoincrement=True)
    name=db.Column(db.String(100),nullable=False) # 名称
    file=db.Column(db.String(256),default='/media/sounds/test.mp3') # 音频路径
    category_id = db.Column(db.Integer, db.ForeignKey('h_category.id'), nullable=False)  # 外键关联用户 ID

    def to_dic(self):
        dic = {
            'id': str(self.id),
            'name': self.name,
            'path': f'/static{self.file}',
            'c_id':self.category_id
        }
        return dic


class VideoCategory(db.Model):
    __tablename__ = 'v_category'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)
    video = db.relationship('Video', backref='video', lazy=True)  # 一对多关系

    def to_dic(self):
        dic = {
            'id': self.id,
            'name': self.name,
        }
        return dic


class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)  # 名称
    file = db.Column(db.String(256), default='/media/video/test.mp4')  # 视频路径
    introduce=db.Column(db.String(256),nullable=True) # 介绍
    category_id = db.Column(db.Integer, db.ForeignKey('v_category.id'), nullable=False)  # 外键关联用户 ID
    def to_dic(self):
        dic = {
            'id': str(self.id),
            'name': self.name,
            'introduce':self.introduce,
            'path': f'/static{self.file}',
        }
        return dic



class Exercises(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)

    def to_dic(self):
        dic = {
            'id': self.id,
            'name': self.name,
        }
        return dic


class QuizCategory(db.Model):
    __tablename__ = 'q_category'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)
    e_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)  # 外键关联用户 ID
    exercises = db.relationship('Exercises', backref='exercises', lazy=True)  # 一对多关系


    def to_dic(self):
        dic = {
            'id': self.id,
            'name': self.name,
        }
        return dic


class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)  # 名称
    opt1=db.Column(db.String(100),nullable=True)
    opt2 = db.Column(db.String(100), nullable=True)
    opt3 = db.Column(db.String(100), nullable=True)
    opt4 = db.Column(db.String(100), nullable=True)
    correct=db.Column(db.String(100),nullable=True) # 正确选项
    file=db.Column(db.String(256),nullable=True) # 音频路径
    category_id = db.Column(db.Integer, db.ForeignKey('q_category.id'), nullable=False)  # 外键关联用户 ID
    category = db.relationship('QuizCategory', backref='category', lazy=True)  # 一对多关系


    def to_dic(self):
        dic = {
            'id': str(self.id),
            'question':self.name,
            'opt_list':self.get_opt_list(),
            'file':None
        }
        if self.file:
            dic['file']=f'/static{self.file}'
        return dic

    def get_opt_list(self):
        lis=[self.opt1,self.opt2]
        if self.opt3:
            lis.append(self.opt3)
        if self.opt4:
            lis.append(self.opt4)
        return lis
