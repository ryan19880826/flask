from flask import Flask #載入flask
app = Flask(__name__) #像是初始app

from flask import render_template #載入flask
from datetime import datetime
@app.route('/hello/<name>') #定義路由 @稱為裝飾器 用途就是把這個網頁路徑結合下一列函式 只要輸入這個網頁路徑就會執行下面的函式 通常會將網頁路徑跟函式名稱取一樣的
def hello(name):
	now = datetime.now()
	return render_template('hello.html', **locals())
if __name__ == '__main__':
        app.run()
