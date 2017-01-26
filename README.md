# DjangoProj
Django Project

create python django project:

sudo easy_install pip

sudo pip install Django==1.10.5

django-admin.py startproject DjangoProj


run project:

python manage.py runserver

python manage.py runserver 0.0.0.0:8000

项目结构:

DjangoProj: 项目的容器。

manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。

DjangoProj/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。

DjangoProj/settings.py: 该 Django 项目的设置/配置。

DjangoProj/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。

DjangoProj/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。



添加model:

python manage.py startapp TestModel



安装MySQL-python:

vi ~/.bash_profile

然后添加:

export PATH=${PATH}:/usr/local/mysql/bin

使更改生效:

source ~/.bash_profile

install MySQL-python

sudo pip install MySQL-python

创建数据库:

python manage.py migrate

注意:syncdb is deprecated because of the migration system.
在Django 1.9及未来的版本种使用migrate代替syscdb.

