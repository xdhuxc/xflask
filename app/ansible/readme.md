### 目的
使用 ansible 时，需要生成 ssh key，用作管理机与被管理机的密钥认证。此脚本的目的在于自动生成 ssh key，并复制到 hosts 中所有主机上，一次性完成被管理机的添加，但是主机的分组不在此脚本范围之内。



### 用法
1、在 hosts 文件中以如下格式添加机器信息
```angular2html
targat_host username password port
或
targat_host username password
```
例如，机器 10.10.24.32 的信息如下：
```angular2html
10.10.24.32 root xdhuxc862 22
```
如果不指定端口，默认为：22

执行该脚本
```angular2html
./install_ansible.sh
```