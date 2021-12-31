from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment
'''
好像就是配置jinja2的环境
'''
# 将jinja2模板设置到项目环境
def environment(**option):
    env = Environment(**option)
    env.globals.update({
        'static':staticfiles_storage.url,
        'url':reverse,
    })
    return env