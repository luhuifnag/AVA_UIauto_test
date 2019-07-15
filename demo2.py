import unittest
class A(unittest.TestCase):

    _result = {}

    def test_001(self):
        self.x = 1
        if self.x >= 0:
            self._result['test_001'] = 'pass'

    @unittest.skipIf(_result['test_001'] == 'pass', '跳过')
    def test_002(self):
        pass

if __name__ == 'main':
    unittest.main()
