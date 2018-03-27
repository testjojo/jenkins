# -*- coding: utf-8 -*-
# 导包pytest
import pytest


# 建类,必须是Test开头,pytest只会执行Test开头的类里面的test开头的方法
class Test:
    # 方法必须是test开头,否则pytest不会认为这是个用例
    def test(self):
        print("-----------结束------------")
        # 添加断言1表示通过,0表示失败
        assert 1


if __name__ == '__main__':
    print("-----------开始--------------")
    # one.py表示执行哪个命令
    pytest.main(["-s", "one.py"])
    # 在命令行输入python one.py执行该文件
