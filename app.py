'''
Author: hszheng hszheng2011@foxmail.com
Date: 2022-12-12 14:18:31
LastEditors: hszheng hszheng2011@foxmail.com
LastEditTime: 2022-12-13 10:57:19
FilePath: /switch-django-crontab/app.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from flask import Flask, request, abort
from flask import render_template
from cron import Cron
import json

app = Flask(__name__, static_folder='static')

@app.route('/')
def hello_world():
    return render_template('index.html', name="hszheng")

@app.route("/cron")
def all_cron():
    try:
        cron = Cron()
        cron_list = cron.select()
        return render_template('index.html', cron_list=cron_list)
    except Exception as e:
        abort(500)

# cron任务操作
@app.route("/opcron", methods=["GET"])
def enable_cron():
    success_msg = ""
    error_msg = ""
    op_type = request.args.get("optype")
    job_id = int(request.args.get("cronid"))
    try:
        crons = Cron()
        if op_type == "0":
            crons.enable_by_id(job_id)
            success_msg = "定时任务-{}-已启用".format(job_id+1)
        elif op_type == "1":
            crons.disable_by_id(job_id)
            success_msg = "定时任务-{}-已停用".format(job_id +1)
        else:
            error_msg = "不支持的操作"
        cron_list = crons.select()
        return render_template('index.html', cron_list=cron_list, success_msg=success_msg, error_msg=error_msg)
    except Exception as e:
        print(e)
        abort(500)

if __name__ =="__main__":
    app.run(debug=True, port=8080, host="192.168.31.211")

