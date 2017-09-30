
CentOS Yum 工具安装，简单方便，官方源列表，RPM LIST。

https://www.postgresql.org/download/linux/redhat/
添加RPM

```
yum install https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm

```

安装PostgreSQL 9.6

postgresql96-server  数据库核心服务端

postgresql96-contrib  附加第三方扩展

postgresql96-devel  C语言开发Header头文件和库


```
yum install postgresql96-server postgresql96-contrib postgresql96-devel
```

验证是否安装成功

rpm -aq| grep postgres
默认Postgresql数据库路径是 /var/lib/pgsql/9.6/data ，可以新建一个目录，假如是/home/pgdata


```
sudo mkdir /home/pgdata
sudo chown -R postgres:postgres /home/pgdata
sudo chmod 700 /home/pgdata


vim /usr/lib/systemd/system/postgresql-9.6.service
```

Environment=PGDATA =/home/pgdata/  修改为自己的新的数据路径
初始化数据库

```
/usr/pgsql-9.6/bin/postgresql96-setup initdb
```

开启服务
```
service postgresql-9.6 start  
或者 systemctl start postgresql-9.6.service
```

开机启动
```
sudo chkconfig postgresql-9.6 on  
或者 systemctl enable postgresql-9.6.service
```


修改密码


```
su postgres
psql
ALTER USER postgres WITH PASSWORD 'wangcz123';   --必须以分号结束，成功执行后会出现ALTER ROLE
\q #退出
exit
su root
```

开启远程访问


```
vim /var/lib/pgsql/9.6/data/postgresql.conf  或者
vim /home/pgdata/postgresql.conf
修改#listen_addresses = 'localhost'  为  listen_addresses='*'
```


当然，此处‘*’也可以改为任何你想开放的服务器IP


信任远程连接

vi /var/lib/pgsql/9.6/data/pg_hba.conf  或者  

```
vim /home/pgdata/pg_hba.conf
```
/IPv4
修改如下内容，信任指定服务器连接
# IPv4 local connections:
host    all            all      127.0.0.1/32      trust（本机无需密码访问）
host    all            all      192.168.16.0/24（16.*皆可访问）  trust
host    all            all      0.0.0.0/0  md5 #（md5加密密码访问）



重启服务
```
service postgresql-9.6 restart
```
或者
systemctl restart postgresql-9.6.service

简单使用：

psql -U postgres postgres  连接数据库

说明：-h表示主机（Host），-p表示端口（Port），-U表示用户（User）

显示所有数据库： \l

卸载
```
yum erase postgresql96
```


https://yum.postgresql.org/9.6/redhat/rhel-6-x86_64/
安装plpythonu


# 端口转发
vim /etc/sysconfig/iptables
ssh  -g -L 45432:localhost:5432 localhost  #转为45432访问
-A INPUT -m state --state NEW -m tcp -p tcp --dport 45432 -j ACCEPT

vim /etc/ssh/sshd_config
service sshd restart
vim /etc/sysconfig/iptables
# Firewall configuration written by system-config-firewall
# Manual customization of this file is not recommended.
*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
-A INPUT -p icmp -j ACCEPT
-A INPUT -i lo -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT
-A INPUT -m state --state NEW -m multiport -p tcp --dport 3306,5432 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT
#NFS service
-A INPUT -p tcp -m multiport --dport 5001,5002,5003 -j ACCEPT
-A INPUT -p udp -m multiport --dport 5001,5002,5003 -j ACCEPT
-A INPUT -p udp -m udp --dport 111 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 111 -j ACCEPT
-A INPUT -p udp -m udp  --dport 2049 -j ACCEPT
-A INPUT -p tcp -m tcp  --dport 2049 -j ACCEPT
-A INPUT -j REJECT --reject-with icmp-host-prohibited
-A FORWARD -j REJECT --reject-with icmp-host-prohibited
COMMIT

service iptables save 进行保存
重启iptables
service iptables save && service iptables restart
查看是否安装了scp，如未安装，可运行yum install scp即可。
将本地文件拷贝到远程
scp 文件名 –用户名@计算机IP或者计算机名称:远程路径
cd /home/pgdata
tar -zcf pgdata.tar.gz  / #打包
scp /home/pgdata/pgdata.tar.gz  root@114.55.33.101:/mnt/pgdata
tar zxf pgdata.tar.gz
mv /mnt/pgdata/home/pgdata/*  /mnt/pgdata
从远程将文件拷回本地
scp –用户名@计算机IP或者计算机名称:文件名 本地路径
复制目录

将本地目录拷贝到远程
scp -r 目录名 用户名@计算机IP或者计算机名称:远程路径
scp -r /home/pgdata root@114.55.33.101:/mnt/pgdata
从远程将目录拷回本地
scp -r 用户名@计算机IP或者计算机名称:目录名 本地路径
打开防火墙

#vim /etc/sysconfig/iptables#编辑防火墙配置文件(centos7以前）

CentOS 防火墙中内置了PostgreSQL服务，配置文件位置在/usr/lib/firewalld/services/postgresql.xml，我们只需以服务方式将PostgreSQL服务开放即可。

systemctl enable firewalld 开机启用防火墙
systemctl start firewalld 开启防火墙
firewall-cmd --add-service=postgresql --permanent   #开放postgresql服务
firewall-cmd --zone=public --add-port=45432/tcp --permanent #开发45432端口
firewall-cmd --zone=public --add-port=54321/tcp --permanent

firewall-cmd --reload  重载防火墙
firewall-cmd --list-ports 查看占用端口
systemctl stop firewalld
