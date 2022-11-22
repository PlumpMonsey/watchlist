from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user')
def hello_user():
    return '<h1>Hello User!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

@app.route('/test')
# 访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL
def test_url_for():
    # 生成 hello 视图函数对应的 URL，将会输出：/
    print(url_for('hello'))
    # 输出：/user
    print(url_for('hello_user'))
    # 输出：/user/Plump
    print(url_for('user_page', name='Plump'))
    # 输出：/test
    print(url_for('test_url_for'))
    # 输出：/test?num=2
    print(url_for('test_url_for', num=2))
    return 'Test Page'