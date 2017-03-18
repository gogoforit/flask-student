from flask import Flask,flash,render_template,request
from models import User
import pymongo
app = Flask(__name__)

app.secret_key = '123'
@app.route('/')
def LoginAndReg():

    return render_template("index.html")


@app.route('/ConfirmNewReg',methods={'POST'})  #注册验证
def ConfirmNewReg():
    form = request.form
    username = form.get('username')
    password = form.get('password')
    if not username:
        flash('please input username')
        return render_template('newregister.html')
    if not password:
        flash('please input password')
        return render_template('newregister.html')
    user = User(username,password)
    confirmseq = user.confirm_user()
    if confirmseq !=None:
        flash('该用户已经注册！请重新注册！')
        return render_template('newregister.html')
    else :
        user = User(username=username, password=password)
        user.save()

        return render_template('AfterRegister.html')


@app.route('/regin',methods={'POST'})  #登陆验证
def regin():
    form = request.form
    username = form.get('username')
    password = form.get('password')
    if not username:
        flash('please input username')
        return render_template('newregister.html')
    if not password:
        flash('please input password')
        return render_template('newregister.html')
    user = User(username, password)
    confirmseq = user.confirm_user()
    if confirmseq==None:
        flash("没有此用户！")
        return render_template('index.html')
    else :
        return render_template('sign.html',user=confirmseq) #返回签到页面

@app.route('/sign',methods={'POST'})
def sign():
    form = request.form
    username = form.get('username')
    User.sign(username)

    return render_template('aftersign.html')


@app.route('/css')
def css():
    return 'hello'


@app.route('/newregister')
def newregister():
    return render_template('newregister.html')

@app.errorhandler(404)
def error_404(e):  #这里有一个异常e
    return render_template('404.html')


if __name__ == '__main__':
    app.run()
