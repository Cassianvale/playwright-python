import os
import pytest


def run():
    pytest.main(['-s', '-W', 'ignore:Module already imported:pytest.PytestWarning',
                 '--alluredir', './report/tmp', "--clean-alluredir"])
    os.system(r"allure generate ./report/tmp -o ./report/html --clean")
    # 程序运行之后，自动启动报告，如果不想启动报告，可注释这段代码
    os.system(f"allure serve ./report/tmp -h 127.0.0.1 -p 9999")


if __name__ == '__main__':
    run()
