# @Author  : kane.zhu
# @Time    : 2022/11/23 18:02
# @Software: PyCharm
# @Description:
import time


from flask import current_app

from src import create_app, make_celery

cele = make_celery(create_app())


@cele.task(name="celery_reverse_string-test")
def reverse(do_string):
    with current_app.app_context():
        time.sleep(10)
        return do_string[::-1]