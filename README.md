# playwright-python

> 虚拟环境: Python 3.8.5 、pytest 7.2.0  

**Roadmap**  

- [x] 封装基础页面组件、log日志  
- [x] 基于pytest-bdd生成测试用例，重构自动生成用例方法
- [ ] 使用OpenAi API根据steps自动生成函数名  
- [ ] 增加自定义函数
- [ ] 生成bdd测试报告
- [ ] 发送测试报告邮件通知  


**本地部署**  
  
下载 Allure [直达链接](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/)，并配置 Allure 环境变量  
```
cd playwright-python
python -m .venv venv
source .venv/Scripts/activate
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pytest-bdd generate tests/features/shop/shop.feature > tests\step_defs\test_shop.py
```

**执行test_cases下的用例**  
```
python run.py
```


**pytest-bdd运行新模板示例(待构建)**
```
python ./utils/generate_testcase.py generate tests/features/shop/shop.feature > tests/step_defs/shop/test_shop.py
```

**常见问题**  
- 如遇到报错`playwright._impl._errors.Error: Executable doesn't exist at C:\...\chrome.exe`，请执行`playwright install`
