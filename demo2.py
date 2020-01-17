#coding:utf-8
'''
Created on 2019年04月16日

@author: Aloe
'''
class base:
    def __init__(self,driver):
        self.driver = driver

    def a(self):
        print('000')

class record(base):

    def b(self):
        print('bbbbb')

class homepage(base):

    def f(self):
        print('fffff')

class operation(record):

    def __init__(self):
        super(operation,self).__init__(self)
        self.home = homepage(self.driver)
  
    def c(self):
        self.home.f()
        
class M(operation):
    def m(self):
        self.c()

# operation().c()
M().m()
        
