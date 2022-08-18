from flask import Flask
import json

app = Flask(__name__)
app.secret_key =b'\x15f\x07\xd3\xd9\xbf*\x82\xd1\xe6\xb4\xf2\x95\xdd\x8f\x12'
#命令行中运行后拷贝出随机值  python -c "import os; print(os.urandom(16))"

@app.route('/hello')
def helloworld():
  returnData = {'code': 0, 'msg': 'success', 'data': 'hello world' }
  return json.dumps(returnData),200

if __name__ == '__main__':
  app.run(debug = True)