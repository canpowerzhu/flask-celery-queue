# @Author  : kane.zhu
# @Time    : 2022/11/23 18:02
# @Software: PyCharm
# @Description:
import time
from log_setting import logger
from celery.schedules import crontab

# todo
# crontab实现定时任务

from flask import current_app

from src import create_app, make_celery

cele = make_celery(create_app())


@cele.task(name="celery_reverse_string-test")
def reverse(do_string):
    with current_app.app_context():
        time.sleep(60)
        return do_string[::-1]


@cele.task(name="celery.reverse_schedule")
def reverse_schedule():
    do_string = "12345678"
    logger.info("celery schedule")
    with current_app.app_context():
        return do_string[::-1]

