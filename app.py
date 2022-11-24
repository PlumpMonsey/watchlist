from flask import Flask, url_for, render_template
from markupsafe import escape

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

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

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
    