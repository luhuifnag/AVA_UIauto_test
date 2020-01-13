#coding:utf-8
'''
Created on 2019年04月16日

@author: Aloe
'''
class A:
    cookies = []
    def a(self):
        global cookies
        c = []
        for i in range(3):
            c.append(i)
        cookies = c

class B(A):

    def b(self):
        print(cookies)

class C(A):

    def b(self):
        print(cookies)


# A().a()
B().b()
C().b()
        
