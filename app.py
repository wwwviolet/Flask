from flask import Flask,render_template
                        #渲染模板
import datetime
app = Flask(__name__)

#路由解析，通过用户访问的路径，匹配相应的函数
@app.route('/test')
def hello_world():
    return '你好'






#debug开启
# @app.route("/index")
# def index():
#     return


#通过访问路径，获取用户的字符串
# @app.route("/user/<name>")
# def hello(name):
#     return "你好，%s"%name

#通过访问路径，获取用户的整型参数，此外还用float类型
# @app.route("/user/<int:id>")
# def welcome(id):
#     return "你好，%d的会员"%id

#路由路径不能重复,用户只能通过唯一路径访问特定的函数

#返回给用户渲染后的网页文件
# @app.route("/")
# def index2():
#     return render_template("index.html")

#向页面传递一个变量
@app.route("/")
def index1():
    time = datetime.date.today()    #普通变量
    name = ["小汪汪","小昭昭"]        #列表类型
    task = {"任务":"打扫卫生"}        #字典类型
    return render_template("index.html",var = time,list = name,task = task)     #传递一个变量等于time


if __name__ == '__main__':
    app.run()
