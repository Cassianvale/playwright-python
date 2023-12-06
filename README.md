# playwright-python

> 虚拟环境：Python 3.8.5 、pytest 7.2.0  

- [x] 封装页面组件、Log日志  
- [ ] 发送测试报告、邮件通知  
- [ ] 附件上传  

**本地部署**  
下载[Allure](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/)，并配置Allure环境  
```
cd playwright-python
python -m .venv venv
source .venv/Scripts/activate
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**开始运行**  
```
python run.py
```

**常见问题**  
- 如遇到报错`playwright._impl._errors.Error: Executable doesn't exist at C:\...\chrome.exe`，请执行`playwright install`