# -*- coding: utf-8 -*-
class Test:
    def setup_class(self):
        print("setup_class1")

    def teardown_class(self):
        print("teardown_class1")

    def setup(self):
        print("------start1------")

    def teardown(self):
        print("------end1--------")

    def test1(self):
        print("-----test1------")


class Test2:
    def setup_class(self):
        print("setup_class2")

    def teardown_class(self):
        print("teardown_class2")

    def setup(self):
        print("------start2------")

    def teardown(self):
        print("------end2--------")

    def test1(self):
        print("-----test2------")
# 运行时用pytest -s setup_teardown.py
