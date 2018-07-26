### bfd.py 

#### 说明
使用 python 编写脚本，查找 linux 系统中的大文件和目录，可支持命令行


#### 用法
```angular2html
-d：指定基础目录，默认为当前目录。
-s，--size=500M：指定目录或文件的最小大小，默认为：500M。
-t，--type=file或--type=directory：指定查找类型，文件或者目录，默认为文件。
-S，--sort=asc或--sort=desc：指定排序规则，默认为：asc
-L，--level：指定层级，默认为当前目录下所有。
-h，--help：输出帮助信息。
```
#### 详解
```angular2html
bfd.py -b 指定目录 

```


### esc.py

#### 说明
清理elasticsearch过期数据

#### 索引格式
```angular2html
zipkin-2018-07-18
app-event-2018.07.17
developer_docker_20180630
doclog-c87e2267-1001-4c70-bb2a-ab41f3b81aa3-2018.06
privatizationlog-c87e2267-1001-4c70-bb2a-ab41f3b81aa3-2018-07-02
privatizationlog-ingress-nginx-2018-07-02
privatizationlog-kube-system-2018-07-02
```
格式抽象：
```angular2html
index_prefix + separator + format_date
```

#### 用法
```angular2html
-i, --index: 指定待删除索引前缀或名称, 必须指定.                 
-s, --separator: 指定索引与日期之间的分隔符, 默认为：-.          
-f, --format: 指定日期格式, 默认为: %Y-%m-%d, 例如: 2018-07-22. 
-H, --host: 指定 elasticsearch 所在主机, 默认为当前主机.        
-p, --port: 指定 elasticsearch 的 HTTP 端口, 默认为: 9200. 
-h, --help: 输出帮助信息. 
```

#### 详解
```angular2html
esc.py -i zinkin             # 删除当前日期之前的所有数据
esc.py -i zinkin 
```
