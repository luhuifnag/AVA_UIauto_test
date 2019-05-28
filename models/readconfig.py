#coding:utf-8
'''
Created on 2019年04月16日

@author: Aloe
'''

import configparser
import os
#RawCnfigParser是最基础的INI文件读取类
conf = configparser.RawConfigParser()

#os.path.join()函数用于路径拼接文件路径。 
# os.path.join()函数中可以传入多个路径：
# 会从第一个以”/”开头的参数开始拼接，之前的参数全部丢弃。
# 以上一种情况为先。在上一种情况确保情况下，若出现”./”开头的参数，会从”./”开头的参数的上一个参数开始拼接。
# os.getcwd() 方法用于返回当前工作目录

#读取文件
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]   
conf.read(os.path.join(BASE_PATH,'models\\configfile.conf'),encoding='UTF-8')



#账号、密码
username = conf.get("login", "username")
password = conf.get("login", "password")

#文件路径
screen_path = os.path.join(BASE_PATH, 'screen')
log_path = os.path.join(BASE_PATH, 'log')
report_path = os.path.join(BASE_PATH, 'report')
logo_upload_path = os.path.join(BASE_PATH, 'date')
software_upload_path = os.path.join(BASE_PATH, 'files')

#url
defaulturl = conf.get("platform", "defaulturl")
url = conf.get("platform", "url")
newurl = conf.get("platform", "newurl")

##rserver注册的相关参数
rserverip = conf.get("rserver", "rserverip")
name = conf.get("rserver", "name")
pwd = conf.get("rserver", "pwd")
machineName = conf.get("rserver", "machineName")

# 更改前的网络参数
netaddr1 = conf.get("network","netaddr1")
netaddr2 = conf.get("network","netaddr2")
netaddr3 = conf.get("network","netaddr3")
netaddr4 = conf.get("network","netaddr4")

subnet1 = conf.get("network","subnet1")
subnet2 = conf.get("network","subnet2")
subnet3 = conf.get("network","subnet3")
subnet4 = conf.get("network","subnet4")

gateway1 = conf.get("network","gateway1")
gateway2 = conf.get("network","gateway2")
gateway3 = conf.get("network","gateway3")
gateway4 = conf.get("network","gateway4")


# 更改后的网络参数
new_netaddr1 = conf.get("network2","new_netaddr1")
new_netaddr2 = conf.get("network2","new_netaddr2")
new_netaddr3 = conf.get("network2","new_netaddr3")
new_netaddr4 = conf.get("network2","new_netaddr4")

new_subnet1 = conf.get("network2","new_subnet1")
new_subnet2 = conf.get("network2","new_subnet2")
new_subnet3 = conf.get("network2","new_subnet3")
new_subnet4 = conf.get("network2","new_subnet4")

new_gateway1 = conf.get("network2","new_gateway1")
new_gateway2 = conf.get("network2","new_gateway2")
new_gateway3 = conf.get("network2","new_gateway3")
new_gateway4 = conf.get("network2","new_gateway4")