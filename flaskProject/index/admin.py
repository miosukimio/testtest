import os.path

from flask_admin.contrib.sqla import ModelView
from flask_admin.form import upload

from index.models import *
from flask_admin import Admin, AdminIndexView
from flask import redirect,session,url_for
import markupsafe
from wtforms import form, fields, validators
from index.config import media_root


class UserAdmin(ModelView):
    # 通过Model和form分别制定数据库表模型和表单模型
    Model = User
    # can_create-允许新建、can_edit-允许修改、can_delete-允许删除、can_view_details-允许查看明细
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    details_modal = True
    # column_list-显示字段、column_details_list-显示明细字段
    # column_labels-字典，以字符形式显示相关字段、column_formatters-字段格式化
    column_list = ('id', 'username','password','email', 'phone','is_admin',)
    column_details_list = ('id', 'username', 'password','email', 'phone','is_admin', )
    column_labels = dict(id='用户ID', username='用户名', password='密码',phone='手机号',email='email',is_admin='管理员')

    def get_admin(view, context, model, name):
        _value = getattr(model, name, None)
        if _value:
            return '是'
        return '否'

    column_formatters = dict(
        is_admin=get_admin,
    )



class HiraganaCategoryAdmin(ModelView):
    Model = HiraganaCategory
    # can_create-允许新建、can_edit-允许修改、can_delete-允许删除、can_view_details-允许查看明细
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    details_modal = True
    # column_list-显示字段、column_details_list-显示明细字段
    # column_labels-字典，以字符形式显示相关字段、column_formatters-字段格式化
    column_list = ('id','name', )
    column_details_list = ('id', 'name', )
    column_labels = dict(id='类别ID', name='类别名称', )



class HiraganaForm(form.Form):
    """
    不能为空:[validators.DataRequired()]
    可以为空:[validators.Optional()]
      description-描述 default-默认值 choice-选择框 coerce-强制转换类型
    注意：如果表单中设置某个字段为FileField，则界面会出现选择文件的界面、SelectField为下拉选择界面，StringField为文本输入
    """
    name = fields.StringField('名称', [validators.DataRequired()])
    category_id = fields.StringField('类别id', [validators.DataRequired()])
    file = upload.FileUploadField('音频',base_path=media_root,default='test.mp3',relative_path='/media/sounds/')



class HiraganaAdmin(ModelView):
    Model = Hiragana
    form = HiraganaForm
    # can_create-允许新建、can_edit-允许修改、can_delete-允许删除、can_view_details-允许查看明细
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    details_modal = True
    # column_list-显示字段、column_details_list-显示明细字段
    # column_labels-字典，以字符形式显示相关字段、column_formatters-字段格式化
    column_list = ('id', 'name','category_id','file', )
    column_details_list = ('id', 'name','category_id','file' )
    column_labels = dict(id='ID', name='名称',category_id='类别', file='音频',)

    def format_image(view, context, model, name):
        _value = getattr(model, name, None)
        img_src=f'/static/{_value}'
        _value = markupsafe.Markup('<audio controls><source src="{}" width="100px" type="audio/mpeg"/></audio>'.format(img_src))
        return _value

    def get_category(self, context, model, name):
        _value=getattr(model, name, None)
        _value=HiraganaCategory.query.filter_by(id=int(_value)).first().name
        return _value


    column_formatters = dict(
        category_id=get_category,
        file=format_image
    )

class VideoCategoryAdmin(ModelView):
    Model = VideoCategory
    # can_create-允许新建、can_edit-允许修改、can_delete-允许删除、can_view_details-允许查看明细
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    details_modal = True
    # column_list-显示字段、column_details_list-显示明细字段
    # column_labels-字典，以字符形式显示相关字段、column_formatters-字段格式化
    column_list = ('id','name', )
    column_details_list = ('id', 'name', )
    column_labels = dict(id='类别ID', name='类别名称', )



class VideoForm(form.Form):
    """
    不能为空:[validators.DataRequired()]
    可以为空:[validators.Optional()]
      description-描述 default-默认值 choice-选择框 coerce-强制转换类型
    注意：如果表单中设置某个字段为FileField，则界面会出现选择文件的界面、SelectField为下拉选择界面，StringField为文本输入
    """
    name = fields.StringField('名称', [validators.DataRequired()])
    introduce=fields.StringField('介绍',[validators.Optional()])
    category_id = fields.StringField('类别id', [validators.DataRequired()])
    file = upload.FileUploadField('视频',base_path=media_root,default='test.mp4',relative_path='/media/video/')



class VideoAdmin(ModelView):
    Model = Video
    form = VideoForm
    # can_create-允许新建、can_edit-允许修改、can_delete-允许删除、can_view_details-允许查看明细
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    details_modal = True
    # column_list-显示字段、column_details_list-显示明细字段
    # column_labels-字典，以字符形式显示相关字段、column_formatters-字段格式化
    column_list = ('id', 'name','category_id','file', )
    column_details_list = ('id', 'name','category_id','file' )
    column_labels = dict(id='ID', name='名称',category_id='类别',introduce='介绍', file='视频路径',)


    def get_category(self, context, model, name):
        _value=getattr(model, name, None)
        _value=VideoCategory.query.filter_by(id=int(_value)).first().name
        return _value


    column_formatters = dict(
        category_id=get_category,
    )




class ExercisesAdmin(ModelView):
    Model = Exercises
    # can_create-允许新建、can_edit-允许修改、can_delete-允许删除、can_view_details-允许查看明细
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    details_modal = True
    # column_list-显示字段、column_details_list-显示明细字段
    # column_labels-字典，以字符形式显示相关字段、column_formatters-字段格式化
    column_list = ('id','name', )
    column_details_list = ('id', 'name', )
    column_labels = dict(id='习题ID', name='习题名称', )


class QuizCategoryForm(form.Form):
    """
    不能为空:[validators.DataRequired()]
    可以为空:[validators.Optional()]
      description-描述 default-默认值 choice-选择框 coerce-强制转换类型
    注意：如果表单中设置某个字段为FileField，则界面会出现选择文件的界面、SelectField为下拉选择界面，StringField为文本输入
    """
    name = fields.StringField('名称', [validators.DataRequired()])
    e_id = fields.StringField('习题名称id', [validators.DataRequired()])



class QuizCategoryAdmin(ModelView):
    Model = QuizCategory
    form = QuizCategoryForm
    # can_create-允许新建、can_edit-允许修改、can_delete-允许删除、can_view_details-允许查看明细
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    details_modal = True
    # column_list-显示字段、column_details_list-显示明细字段
    # column_labels-字典，以字符形式显示相关字段、column_formatters-字段格式化
    column_list = ('id','name','e_id' )
    column_details_list = ('id', 'name','e_id' )
    column_labels = dict(id='类别ID', name='类别名称',e_id='所属习题' )

    def get_category(self, context, model, name):
        _value=getattr(model, name, None)
        _value=Exercises.query.filter_by(id=int(_value)).first().name
        return _value


    column_formatters = dict(
        e_id=get_category,
    )


class QuizForm(form.Form):
    """
    不能为空:[validators.DataRequired()]
    可以为空:[validators.Optional()]
      description-描述 default-默认值 choice-选择框 coerce-强制转换类型
    注意：如果表单中设置某个字段为FileField，则界面会出现选择文件的界面、SelectField为下拉选择界面，StringField为文本输入
    """
    name = fields.StringField('题目', [validators.DataRequired()])
    opt1=fields.StringField('选项1', [validators.DataRequired()])
    opt2 = fields.StringField('选项2', [validators.DataRequired()])
    opt3 = fields.StringField('选项3', [validators.Optional()])
    opt4 = fields.StringField('选项4', [validators.Optional()])
    correct = fields.StringField('正确选项', [validators.DataRequired()])
    category_id = fields.StringField('类别id', [validators.DataRequired()])
    file = upload.FileUploadField('音频', base_path=media_root, default='', relative_path='/media/sounds/')




class QuizAdmin(ModelView):
    Model = Quiz
    form = QuizForm
    # can_create-允许新建、can_edit-允许修改、can_delete-允许删除、can_view_details-允许查看明细
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    details_modal = True
    # column_list-显示字段、column_details_list-显示明细字段
    # column_labels-字典，以字符形式显示相关字段、column_formatters-字段格式化
    column_list = ('id', 'name','category_id','opt1', 'opt2','opt3','opt4','correct',)
    column_details_list = ('id', 'name','category_id','opt1', 'opt2','opt3','opt4','correct')
    column_labels = dict(id='ID', name='题目',category_id='所属类别',opt1='选项1',opt2='选项2',opt3='选项3',opt4='选项4',correct='正确答案')


    def get_category(self, context, model, name):
        _value=getattr(model, name, None)
        _value=QuizCategory.query.filter_by(id=int(_value)).first().name
        return _value


    column_formatters = dict(
        category_id=get_category,
    )







class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        user_id = session.get('user_id', '')
        if user_id == '':
            return False
        user = User.query.filter_by(id=user_id).first()
        if not user or not user.is_admin:
            return False
        return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/login_register')

def register_admin(app):

    admin = Admin(app, name='管理后台', template_mode='bootstrap3',index_view=MyAdminIndexView(),url='/admin')
    admin.add_view(UserAdmin(User, db.session,name='用户管理'))
    admin.add_view(HiraganaCategoryAdmin(HiraganaCategory, db.session, name='五十音类别管理'))
    admin.add_view(HiraganaAdmin(Hiragana, db.session,name='五十音管理'))
    admin.add_view(VideoCategoryAdmin(VideoCategory, db.session, name='课程学习类别管理'))
    admin.add_view(VideoAdmin(Video, db.session,name='课程学习管理'))
    admin.add_view(ExercisesAdmin(Exercises,db.session,name='日语习题名称管理'))
    admin.add_view(QuizCategoryAdmin(QuizCategory, db.session, name='日语习题类别管理'))
    admin.add_view(QuizAdmin(Quiz, db.session,name='日语习题管理'))


