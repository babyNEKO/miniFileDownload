from flask import Flask, render_template, send_file, url_for, jsonify, redirect, __version__
from os import listdir
from Modules import conf
import platform
"""
    先配置好conf文件再启动程序
"""
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET'])
def index():
    info = platform.python_version() + " Flask@" + __version__
    return render_template('index.html', title=conf.SITE_NAME, lang=conf.LANGUAGE, info=info)


@app.route('/get_file/<name>', methods=['GET'])
def get_file(name):
    try:
        this_file = conf.QUERY_FILE + name
        return send_file(this_file)
    except PermissionError:
        return not_allowed(405)
    except FileNotFoundError:
        return not_found(404)
    except OSError:
        return not_allowed(405)


@app.route('/get_file/', methods=['GET'])
def redirect_get_file():
    return redirect(url_for('index'))


@app.route('/get_list', methods=['GET'])
def get_list():
    try:
        files = listdir(conf.MAIN_DIR)
        for x in conf.FORBIDDEN_FILES:
            if x in files:
                files.remove(x)
        counter = len(files)
        return jsonify({"counter": counter, "file_list": files})
    except FileNotFoundError:
        msg = "根目录读取失败"
        return jsonify({"message:": msg})


@app.route('/get_list/', methods=['GET'])
def redirect_get_list():
    return redirect(url_for('get_list'))


@app.errorhandler(405)
def not_allowed(error):
    return jsonify({"ERROR": "405"}), 405


@app.errorhandler(404)
def not_found(error):
    return jsonify({"ERROR": "404"}), 404


if __name__ == '__main__':
    app.run()
