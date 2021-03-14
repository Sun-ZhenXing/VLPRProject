# -----流程-----
# cli: 树莓派绑定摄像头程序每1秒截获一张图片
# cli: 上传到Flask服务器
# ser: 服务器检查车牌信息，并检索MySQL服务器
# ser: 检索出信息，反馈到树莓派
# inf: <int> vaild_day          允许天数
# inf: <date> reg_date          注册日期
# inf: <key:int, auto+> vpid    ID
# inf: <varchar> user_name      用户名称
# inf: <varchar> user_phone     用户手机号
# ser:
from flask import Flask, request, send_from_directory, render_template
from flask import jsonify
import os.path
import sys, re, json
from gevent import pywsgi
from mysql_conn import esc_str, sql_exec


app = Flask(__name__, template_folder='templates', static_folder='static')
root = os.path.abspath(__file__)
print('[Info] Root:', root)


@app.route('/', methods=['GET', 'POST'])
def index():
    return send_from_directory('index.html')


@app.route('/upload_files', methods=['GET', 'POST'])
def upload_files():
    '''
    上传图片，并在数据库中查找该车牌信息
    如果
    '''
    if request.method == 'GET':
        return jsonify({'code': 1, 'msg': '错误！只支持POST方法'}), 400
    f = request.files['file']
    f.save(os.path.join(root, 'upload', f.filename))
    return jsonify({
        'code': 0,
        'msg': '上传成功',
        'data': {'src': f'upload/{f.filename}'},
        'files': {'file': f.filename}
    })


@app.route('/reg_info', methods=['GET', 'POST'])
def reg_info():
    '''
    用于上传，更新数据库信息
    '''
    if request.method == 'POST':
        return jsonify({'code': 1, 'msg': '错误！只支持GET方法'}), 400
    username = request.args.get('username')
    userinfo = request.args.get('userinfo')
    try:
        json_obj = json.loads(userinfo)
    except:
        return jsonify({'code': 1, 'msg': '错误！不支持的json对象'})


@app.route('/', methods=['GET', 'POST'])
def file():
    '''

    '''



@app.route('/<path:filename>', methods=['GET', 'POST'])
def retuenFile(filename):
    return send_from_directory(filename)


if __name__ == '__main__':
    from utils import server_setting
    ip = server_setting['host']
    port = server_setting['port']
    server = pywsgi.WSGIServer((ip, port), app)
    print('[Info] Server start...')
    server.serve_forever()
