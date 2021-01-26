Example of the route and wsgi for http server
=========
##学习route与wsgi的小用例
###Get Started
```bash
$ git clone https://github.com/freelizhun/wsgi-route-learning.git

$ cd wsgi-route-learning

$ git checkout with-uwsgi

$ virtualenv venv

$ source venv/bin/activate

$ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requirements.txt 
```
###用uwsgi从后台启动并写入到日志文件
```bash
$ uwsgi --yaml uwsgi_test.yml --daemonize /tmp/my_uwsgi.log
```
浏览器输入http://192.168.108.131:8080/user/login观察测试结果
###关闭与重启uwsgi
```bash
$ uwsgi --stop uwsgi/uwsgi.pid
$ uwsgi --reload uwsgi/uwsgi.pid
```
