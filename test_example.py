import os
import shutil
import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        self.test_dir = "testing/"
        os.mkdir(self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        os.remove("test_example.pyc")

    def test_something(self):
        assert os.path.exists(self.test_dir)
