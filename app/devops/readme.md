### big_fd.py 

#### 说明
使用 python 编写脚本，查找 linux 系统中的大文件和目录，可支持命令行


#### 用法
```angular2html

```

### clean_es_outofdate_date.py

#### 说明
清理elasticsearch过期数据

索引格式如下：
```angular2html
zipkin-2018-07-18
app-event-2018.07.17
developer_docker_20180630
doclog-c87e2267-1001-4c70-bb2a-ab41f3b81aa3-2018.06
privatizationlog-c87e2267-1001-4c70-bb2a-ab41f3b81aa3-2018-07-02
privatizationlog-ingress-nginx-2018-07-02
privatizationlog-kube-system-2018-07-02
```
格式改造：
```angular2html
zipkin - 2018-07-18
app-event - 2018.07.17
developer_docker _ 20180630
doclog-c87e2267-1001-4c70-bb2a-ab41f3b81aa3 - 2018.06
privatizationlog-c87e2267-1001-4c70-bb2a-ab41f3b81aa3 - 2018-07-02
privatizationlog-ingress-nginx - 2018-07-02
privatizationlog-kube-system - 2018-07-02
```


#### 用法
```angular2html
-i：指定索引名称，必须指定。
-s：指定索引与日期之间的分隔符，默认为：-。
-f：指定日期格式，默认为：
```

详解：
```angular2html
clean_es_outofdate_data.py -i zinkin             # 删除当前日期之前的所有数据
clean_es_outofdate_data.py -i zinkin 
```