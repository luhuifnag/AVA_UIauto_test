import unittest
import functools
class test000(unittest.TestCase):

    def skipTest(self,value):
        def deco(function):
            def wrapper(self, *args, **kwargs):
                if not getattr(self, value):
                    self.skipTest('跳过用例')
                else:
                    function(self, *args, **kwargs)
            return wrapper
        return deco

    def test0(self):
        try:
            2<3
        except:
            pass

    @skipTest("test0")
    def test2(self):
        print("123456")
            
if __name__ == "__main__":
   unittest.main()