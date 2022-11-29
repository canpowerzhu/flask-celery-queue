# @Author  : kane.zhu
# @Time    : 2022/11/24 15:51
# @Software: PyCharm
# @Description:
import json

from flask import jsonify, Blueprint,current_app


task_bp = Blueprint('task_bp', __name__)



@task_bp.route('/process/<name>')
def process(name):  # put application's code here
    from tasks.task import reverse
    task = reverse.delay(name)

    return jsonify({'msg:': 'i send an asyn request', 'taskId': task.task_id})


@task_bp.route('/schedule/<name>')
def process_schedule(name):  # put application's code here
    from tasks.task import reverse_schedule
    task = reverse_schedule.delay(name)

    return jsonify({'msg:': 'i send an asyn request', 'taskId': task.task_id})

@task_bp.route('/task_status/<taskId>', methods=['GET'])
def get_add(taskId):
    from tasks.task import reverse
    task_result = reverse.AsyncResult(taskId)
    print(task_result.backend)
    result = {
        'code': 200,
        'msg': 'success',
        'TaskId': taskId,
        'Status': task_result.status,
        'Result': task_result.result
    }
    return jsonify(result)
