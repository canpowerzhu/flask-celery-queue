## Flask+Celery+Redis
### Celery
#### 启动worker
```shell
[2022-11-24 16:36:05,125: INFO/SpawnPoolWorker-31] process 17732 exiting with exitcode 1
(venv) PS F:\pythonCode\pythonProject\flaskProject\flaskProject\flask-celery-queue> celery -A celery_tasks.task worker --loglevel=info

 -------------- celery@KaneZhu v5.2.7 (dawn-chorus)
--- ***** -----
-- ******* ---- Windows-10-10.0.19041-SP0 2022-11-24 16:42:56
- *** --- * ---
- ** ---------- [config]
- ** ---------- .> app:         app:0x2ed91161988
- ** ---------- .> transport:   redis://192.168.1.4:6369/1
- ** ---------- .> results:     redis://192.168.1.4:6369/1
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor celery_tasks in this worker)
--- ***** -----
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery


[celery_tasks]
  . celery_tasks.task.reverse

[2022-11-24 16:42:56,856: INFO/MainProcess] Connected to redis://192.168.1.4:6369/1
[2022-11-24 16:42:56,863: INFO/MainProcess] mingle: searching for neighbors
[2022-11-24 16:42:57,005: INFO/SpawnPoolWorker-1] child process 18380 calling self.run()
[2022-11-24 16:42:57,148: INFO/SpawnPoolWorker-2] child process 10512 calling self.run()
[2022-11-24 16:42:57,271: INFO/SpawnPoolWorker-3] child process 9324 calling self.run()
[2022-11-24 16:42:57,332: INFO/SpawnPoolWorker-4] child process 10064 calling self.run()
[2022-11-24 16:42:57,929: INFO/MainProcess] mingle: all alone
[2022-11-24 16:42:57,942: INFO/MainProcess] celery@KaneZhu ready.
[2022-11-24 16:43:07,810: INFO/MainProcess] Task celery_tasks.task.reverse[b6400d3f-fbdf-4ab3-ab11-70dbeac098ec] received
[2022-11-24 16:43:09,159: INFO/SpawnPoolWorker-5] child process 17524 calling self.run()
[2022-11-24 16:43:09,165: INFO/SpawnPoolWorker-6] child process 4492 calling self.run()
[2022-11-24 16:43:09,180: INFO/SpawnPoolWorker-7] child process 10648 calling self.run()
```

### FAQ
1. celery任务state在windows一直处于pending
 
切换模式 —P threads 即可解决
```shell
celery -A tasks.task worker --loglevel=info -P threads
```

2. 如何启用flower进行监控任务状态
```shell
celery -A tasks.task flower --address=0.0.0.0 --port=5555
```