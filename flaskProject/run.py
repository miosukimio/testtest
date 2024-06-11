import json

from flask import render_template, request, redirect,jsonify,session
from index import app
from index.models import *








@app.route('/')
@app.route('/home')
def home():
    # 渲染首页
    return render_template('home.html')


@app.route('/login_register',methods=['GET','POST'])
def login_register():
    if request.method == 'GET':
        # 渲染登录和注册界面
        return render_template('login_and_register.html')
    else:
        dic={'code':200,'msg':'登录成功'}
        username=request.form.get('username')
        password=request.form.get('password')
        user = User.query.filter_by(username=username,password=password).first()
        if not user:
            dic['code']=0
            dic['msg']='用户名或密码错误'
        else:
            session['user_id']=user.id
        return jsonify(dic)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        dic = {'code': 200, 'msg': '注册成功'}
        username=request.form.get('username')
        password=request.form.get('password')
        phone=request.form.get('phone')
        email=request.form.get('email')
        user=User.query.filter_by(username=username).first()
        if user:
            dic['code']=100
            dic['msg']='用户名已存在'
        else:
            user=User(username=username,password=password,phone=phone,email=email)
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
        return jsonify(dic)

@app.route('/language_selection')
def language_selection():
    user_id=session.get('user_id','')
    if user_id == '':
        return redirect('/login_register')
    return render_template('language_selection.html')


@app.route('/learn')
def learn():
    user_id=session.get('user_id','')
    if user_id == '':
        return redirect('/login_register')
    # 渲染学习页面

    return render_template('learn.html')

@app.route('/hiragana')
def hiragana():
    user_id=session.get('user_id','')
    if user_id == '':
        return redirect('/login_register')
    data={}
    h_list=HiraganaCategory.query.all()
    for h in h_list:
        data[h.name]=[x.to_dic() for x in Hiragana.query.filter_by(category_id=h.id).all()]
    return render_template('hiragana.html',data=data)

@app.route('/save_hiragana',methods=['POST'])
def save_hiragana():
    user_id=session.get('user_id','')
    if user_id == '':
        return redirect('/login_register')
    h_id=request.form.get('h_id')
    hiragana=Hiragana.query.filter_by(id=int(h_id)).first()
    if hiragana:
        user=User.query.filter_by(id=int(user_id)).first()
        dic=user.get_hiragana_dic()
        h_id=int(h_id)
        if h_id in dic:
            dic[h_id]+=1
        else:
            dic[h_id]=1
        user.hiragana_dic=str(dic)
        user.hiragana_time=datetime.datetime.now()
        db.session.commit()
    return jsonify({})

@app.route('/levels')
def levels():
    user_id=session.get('user_id','')
    if user_id == '':
        return redirect('/login_register')
    user = User.query.filter_by(id=int(user_id)).first()
    id=request.args.get('id')
    if not id:
        if user.last_video:
            id=Video.query.filter_by(id=int(user.last_video)).first().category_id
        else:
            id=1
    v_category=VideoCategory.query
    levels_list=[x.to_dic() for x in v_category.all() if x.id != int(id)]
    data=[x.to_dic() for x in Video.query.filter_by(category_id=int(id)).all()]
    return render_template('levels.html',data=data,levels=v_category.filter_by(id=int(id)).first().name,levels_list=levels_list)

@app.route('/save_last_levels',methods=['POST'])
def save_last_levels():
    user_id=session.get('user_id','')
    if user_id == '':
        return redirect('/login_register')
    v_id=request.form.get('v_id')
    video=Video.query.filter_by(id=int(v_id)).first()
    if video:
        user=User.query.filter_by(id=int(user_id)).first()
        user.last_video=v_id
        user.video_time=datetime.datetime.now()
        db.session.commit()
    return jsonify({})


@app.route('/quiz',methods=['GET'])
def quiz():
    user_id=session.get('user_id','')
    if user_id == '':
        return redirect('/login_register')

    id=request.args.get('id')
    c=QuizCategory.query.filter_by(id=int(id)).first()
    data=[x.to_dic() for x in Quiz.query.filter_by(category_id=int(id))]
    return render_template('quiz.html',data=data,title=c.name,c_id=c.id)

@app.route('/select_quiz')
def select_quiz():
    user_id=session.get('user_id','')
    if user_id == '':
        return redirect('/login_register')
    lis=[x.to_dic() for x in Exercises.query.all()]
    return render_template('quiz_selection.html',data=lis)


@app.route('/select_quiz2')
def select_quiz2():
    user_id=session.get('user_id','')
    if user_id == '':
        return redirect('/login_register')
    id = request.args.get('id')
    lis=[x.to_dic() for x in QuizCategory.query.filter_by(e_id=int(id)).all()]
    return render_template('quiz_selection2.html',data=lis)

@app.route('/check_quiz',methods=['POST'])
def check_quiz():
    user_id=session.get('user_id','')
    if user_id == '':
        return redirect('/login_register')
    data=request.form.get('data')
    c_id=request.form.get('c_id')
    data=json.loads(data)
    quiz_list={x.id:x.correct for x in Quiz.query.filter_by(category_id=int(c_id)).all()}
    score=0
    for k,v in quiz_list.items():
        id=str(k)
        if id in data:
            if data[id] == v:
                score+=1
    if quiz_list:
        user=User.query.filter_by(id=int(user_id)).first()
        dic=user.get_score_dic()
        c_id=int(c_id)
        dic[c_id]={'score':score,'time':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        user.score_dic=str(dic)
        db.session.commit()
    return jsonify({'msg':f'您本次习题的最终得分是：<i style="color:red;font-size:15px;">{score}</i>'})

@app.route('/progress')
def progress():
    user_id=session.get('user_id','')
    if user_id == '':
        return redirect('/login_register')
    user=User.query.filter_by(id=int(user_id)).first()
    hiragana_dic=user.get_hiragana_dic()
    hiragana_list=[k for k,v in hiragana_dic.items() if v>=5]
    hiragana=f'{len(hiragana_list)}/{len(Hiragana.query.all())}'

    last_video_id=user.last_video
    levels='未学习'
    if last_video_id:
        video=Video.query.filter_by(id=int(last_video_id)).first()
        levels=f'{VideoCategory.query.filter_by(id=video.category_id).first().name}-{video.name}'

    score_dic=user.get_score_dic()
    score_dic={f'{QuizCategory.query.filter_by(id=k).first().exercises.name}-{QuizCategory.query.filter_by(id=k).first().name}':v for k,v in score_dic.items()}
    return render_template('progress.html',levels=levels,levels_time=user.video_time or '',hiragana=hiragana,hiragana_time=user.hiragana_time or '',quiz=score_dic)

@app.route('/speech')
def speech():
    user_id=session.get('user_id','')
    if user_id == '':
        return redirect('/login_register')
    return render_template('speech.html')





if __name__ == '__main__':
    app.run(debug=True)
