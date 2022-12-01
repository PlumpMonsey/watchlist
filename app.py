import os
import sys
import click

from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape





WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

# 初始化拓展，传入实例程序 app
db = SQLAlchemy(app)

class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份



# 创建虚拟数据
@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()
    name = 'Plump'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    # 用户
    user = User(name = name)
    db.session.add(user)
    # 电影
    for m in movies:
        movie = Movie(title = m['title'], year = m['year'])
        db.session.add(movie)
    
    db.session.commit()
    click.echo('Done.')



@app.cli.command()  # 注册为命令，可以传入 name 参数来自定义命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息



@app.route('/')
def index():
    # <模型类>.query.<过滤方法（可选）>.<查询方法>
    user = User.query.first()   # 读取用户信息
    movies  = Movie.query.all() # 读取电影信息
    return render_template('index.html', user=user, movies=movies)

# @app.route('/')
# def hello():
#     return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

# @app.route('/user')
# def hello_user():
#     return '<h1>Hello User!</h1><img src="http://helloflask.com/totoro.gif">'

# @app.route('/user/<name>')
# def user_page(name):
#     return f'User: {escape(name)}'

# @app.route('/test')
# # 访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL
# def test_url_for():
#     # 生成 hello 视图函数对应的 URL，将会输出：/
#     print(url_for('hello'))
#     # 输出：/user
#     print(url_for('hello_user'))
#     # 输出：/user/Plump
#     print(url_for('user_page', name='Plump'))
#     # 输出：/test
#     print(url_for('test_url_for'))
#     # 输出：/test?num=2
#     print(url_for('test_url_for', num=2))
#     return 'Test Page'
    