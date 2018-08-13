### xflask

### 程序启动方式
```angularjs
python xflask.py runserver --host 0.0.0.0 --port 1994
```

### 其他命令

```angular2html
pip freeze > requirements.txt
```

```angular2html
pip install -r requirements.txt
```

### 扩展安装
需要在虚拟环境中安装
```angularjs

```
### 数据库迁移
1、migrate 子命令用于自动创建迁移脚本
```angularjs
python xflask.py db migrate
```
2、把迁移应用到数据库中，且不影响其中保存的数据
```angularjs
python xflask.py db migrate
```
