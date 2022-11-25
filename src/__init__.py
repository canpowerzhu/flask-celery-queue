from flask import Flask

from conf import config
from src.views import task_bp
from celery import Celery

def make_celery(app):
    cele = Celery(app.import_name, backend=config.CELERY_RESULT_BACKEND,
                  broker=config.BROKER_URL)
    cele.conf.update(app.config)
    TaskBase = cele.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    cele.Task = ContextTask
    return cele


def create_app():
    app = Flask(__name__)
    app.register_blueprint(task_bp)
    return app


