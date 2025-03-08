# wsgi.py

# pylint: disable=missing-docstring

from flask import Flask, render_template, request
from longest_word.game import Game

app = Flask(__name__)

#创建了一个Flask应用实例
@app.route('/')
def home():
    """定义了根路径"/"的处理函数
    当用户访问网站首页时，会创建一个Game实例
    然后渲染名为'home.html'的模板，并将game.grid传递给模板（一个字母网格）
    """
    game = Game()
    return render_template('home.html', grid = game.grid)

#检查路由
@app.route('/check', methods=['POST'])
#定义了"/check"路径的处理函数，并指定只接受POST请求

def check():
    """
    创建一个新的Game实例
    从表单数据中获取'grid'参数并将其转换为列表，然后设置为game.grid
    从表单数据中获取用户输入的'word'参数
    调用game.is_valid(word)方法来检查单词是否有效
    渲染'check.html'模板，并传递检查结果(is_valid)、网格(grid)和单词(word)
    """
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    return render_template('check.html', is_valid=is_valid,
                        grid=game.grid,
                        word=word)
