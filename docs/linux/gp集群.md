#
GREENPLUM总体结构：




数据库由Master Severs和Segment Severs通过Interconnect互联组成。
Master主机负责：建立与客户端的连接和管理；SQL的解析并形成执行计划；执行计划向Segment的分发收集Segment的执行结果；Master不存储业务数据，只存储数据字典。
Segment主机负责：业务数据的存储和存取；用户查询SQL的执行。
master node高可用，类似于hadoop的namenode和second namenode，实现主备的高可用。
Greenplum使用MPP架构：




1、准备
　　这里准备了3台服务器，1台做master，2台做存储（其中1台兼做standby）

OS: centos7
GP: greenplum5.0
JDK:1.8

192.168.244.110 node01                 #master node
192.168.244.111 node02                 #segment node
192.168.244.112 node03                 #segment node（standby）

## 准备1： 关闭SELINUX
vim /etc/selinux/config
SELINUX=disabled
## 准备2： 关闭防火墙 iptables、firewall
chkconfig --list iptables
chkconfig --level 0123456 iptables off

## 准备3： 修改内核参数
kernel.shmmax = 500000000
kernel.shmmni = 4096
kernel.shmall = 4000000000
kernel.sem = 250 512000 100 2048
kernel.sysrq = 1
kernel.core_uses_pid = 1
kernel.msgmnb = 65536
kernel.msgmax = 65536
kernel.msgmni = 2048
net.ipv4.tcp_syncookies = 1
net.ipv4.conf.default.accept_source_route = 0
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_max_syn_backlog = 4096
net.ipv4.conf.all.arp_filter = 1
net.ipv4.ip_local_port_range = 10000 65535
net.core.netdev_max_backlog = 10000
net.core.rmem_max = 2097152
net.core.wmem_max = 2097152
vm.overcommit_memory = 2

## 准备4：修改Linux最大限制

[root@node01 ~]# vi /etc/security/limits.conf
#greenplum configs
* soft nofile 65536
* hard nofile 65536
* soft nproc 131072
* hard nproc 131072


## 准备5：I/O调整优化
[root@node01 ~]# vim /boot/grub/menu.lst
#greenplum configs
elevator=deadline

重启系统使配置生效
reboot

# 安装步骤
## 1 添加所有节点到HOST
[root@node01 ~]# vi /etc/hosts
192.168.244.110 node01
192.168.244.111 node02
192.168.244.112 node03

## 2 GP安装
　　GP的安装操作都是在主节点master上执行的
3.1.创建gpadmin用户
所有节点创建gpadmin用户
[root@node01 ~]# useradd gpadmin
[root@node01 ~]# passwd gpadmin

3.2.设置gpadmin用户环境

[gpadmin@node01 ~]$ cd /home/gpadmin
[gpadmin@node01 ~]$ vim .bashrc
[gpadmin@node01 ~]$ vim .bash_profile

.bashrc和.bash_profile最后都添加下面两行
source /usr/local/greenplum-db/greenplum_path.sh
export MASTER_DATA_DIRECTORY=/data1/gpdata/master/gpseg-1

/etc/profile也添加上面两行内容

设置完后记得source一下使其立即生效

3.3.上传并解压安装包
将greenplum-db-4.3.8.2-build-1-RHEL5-x86_64.zip上传至master的/opt/目录下
[root@node01 opt]# unzip greenplum-db-4.3.8.2-build-1-RHEL5-x86_64.zip
[root@node01 opt]#/bin/bash greenplum-db-4.3.8.2-build-1-RHEL5-x86_64.bin
按提示输入回车或yes 这一步会将安装包解压到/usr/local/下，并建立软连接greenplum-db


3.4.准备节点服务器信息文件
后面的批量安装会用到这两个文件，如果all_host和all_segment内容一样，可以只创建一个文件

[root@node01 greenplum-db]# mkdir -p /opt/gpinst/ [root@node01 gpinst]# touch all_host
[root@node01 gpinst]# touch all_segment
all_host和all_segment内容：
node01
node02
node03
node04

3.5.建立节点服务器间的信任
[root@node01 gpinst]# gpssh-exkeys -f /opt/gpinst/all_host
[STEP 1 of 5] create local ID and authorize on local host

[STEP 2 of 5] keyscan all hosts and update known_hosts file

[STEP 3 of 5] authorize current user on remote hosts
  ... send to node02
  ***
  *** Enter password for node02:
  ... send to node03
  ... send to node04

[STEP 4 of 5] determine common authentication file content

[STEP 5 of 5] copy authentication files to all remote hosts
  ... finished key exchange with node02
  ... finished key exchange with node03
  ... finished key exchange with node04

[INFO] completed successfully
按照提示输入root密码，记住这一步不能输入gpadmin的密码，因为批量安装时需要在/usr/local下创建目录，需要root权限

3.6.批量安装
[root@node01 gpinst]# gpseginstall -f /opt/gpinst/all_host -u gpadmin -p gpadmin
20170717:13:13:51:026424 gpseginstall:node01:root-[INFO]:-Installation Info:
link_name greenplum-db
binary_path /usr/local/greenplum-db-4.3.8.2
binary_dir_location /usr/local
binary_dir_name greenplum-db-4.3.8.2
20170717:13:13:51:026424 gpseginstall:node01:root-[INFO]:-check cluster password access
。。。。。。


20170717:13:16:39:026424 gpseginstall:node01:root-[INFO]:-SUCCESS -- Requested commands completed

这一步其实就是将master上的greenplum打包通过scp命令传到all_host中的主机上，并赋予目录gpadmin的权限

3.7.检查批量安装情况
[root@node01 local]# gpssh -f /opt/gpinit/all_host -e ls -l $GPHOME
[root@node01 gpinst]# gpssh -f /opt/gpinst/all_host -e ls -l $GPHOME
[node01] ls -l /usr/local/greenplum-db/.
[node01] total 276
[node01] drwxr-xr-x 4 gpadmin gpadmin   4096 May 10  2016 bin
[node01] drwxr-xr-x 2 gpadmin gpadmin   4096 May 10  2016 demo
[node01] drwxr-xr-x 5 gpadmin gpadmin   4096 May 10  2016 docs
[node01] drwxr-xr-x 2 gpadmin gpadmin   4096 May 10  2016 etc
[node01] drwxr-xr-x 3 gpadmin gpadmin   4096 May 10  2016 ext
[node01] -rw-r--r-- 1 gpadmin gpadmin  43025 May 10  2016 GPDB-LICENSE.txt
[node01] -rw-r--r-- 1 gpadmin gpadmin    735 Jul 17 13:06 greenplum_path.sh
[node01] drwxr-xr-x 6 gpadmin gpadmin   4096 May 10  2016 include
[node01] drwxr-xr-x 9 gpadmin gpadmin   4096 May 10  2016 lib
[node01] -rw-r--r-- 1 gpadmin gpadmin 192912 May 10  2016 LICENSE.thirdparty
[node01] drwxr-xr-x 2 gpadmin gpadmin   4096 May 10  2016 sbin
[node01] drwxr-xr-x 4 gpadmin gpadmin   4096 May 10  2016 share
[node02] ls -l /usr/local/greenplum-db/.
[node02] total 276
[node02] drwxr-xr-x 4 gpadmin gpadmin   4096 May 10  2016 bin
[node02] drwxr-xr-x 2 gpadmin gpadmin   4096 May 10  2016 demo
[node02] drwxr-xr-x 5 gpadmin gpadmin   4096 May 10  2016 docs
返回结果中各节点目录一致则成功

3.8.创建存储目录

master
[root@node01 gpinst]# mkdir -p /data/gpdata/master
[root@node01 gpinst]# chown gpadmin:gpadmin /data/gpdata/master

segment
[root@node01 gpinst]# gpssh -f /opt/gpinst/all_host -e 'mkdir -p /data/gpdata/primary'
[node04] mkdir -p /data/gpdata/primary
[node02] mkdir -p /data/gpdata/primary
[node01] mkdir -p /data/gpdata/primary
[node03] mkdir -p /data/gpdata/primary

[root@node01 gpinst]# gpssh -f /opt/gpinst/all_host -e 'chown gpadmin:gpadmin /data/gpdata/primary'

[node01] chown gpadmin:gpadmin /data/gpdata/primary
[node02] chown gpadmin:gpadmin /data/gpdata/primary
[node04] chown gpadmin:gpadmin /data/gpdata/primary
[node03] chown gpadmin:gpadmin /data/gpdata/primary

mirror
[root@node01 local]# gpssh -f /opt/gpinit/all_segment -e 'mkdir -p /data1/gpdata/mirror'
[root@node01 local]# gpssh -f /opt/gpinit/all_segment -e 'chown gpadmin:gpadmin /data1/gpdata/mirror'



#3.9.设置时钟同步

vi /etc/ntp.conf 在server第一行添加下面两行
server 192.168.244.110
重启ntpd服务 /etc/init.d/ntpd restart
查看ntp同步情况 ntpq -p
使ntpd服务重启服务器后也启动 chkconfig --level 0123456 ntpd on


3.10.创建并修改GP初始化文件
[root@node01 gpadmin]# su - gpadmin
[gpadmin@node01 ~]$ mkdir /home/gpadmin/gpconfigs
[gpadmin@node01 ~]$ ll
total 4
drwxrwxr-x 2 gpadmin gpadmin 4096 Jul 17 13:30 gpconfigs
[gpadmin@node01 ~]$ cp /usr/local/greenplum-db/docs/cli_help/gpconfigs/gpinitsystem_config /home/gpadmin/gpconfigs/
[gpadmin@node01 ~]$ chmod 775 /home/gpadmin/gpconfigs/gpinitsystem_config

修改GP初始化文件

[gpadmin@node01 ~]$ vi gpconfigs/gpinitsystem_config

declare -a DATA_DIRECTORY=(/data/gpdata/primary /data/gpdata/primary /data1/prim# FILE NAME: gpinitsystem_config

# Configuration file needed by the gpinitsystem

################################################
#### REQUIRED PARAMETERS
################################################

#### Name of this Greenplum system enclosed in quotes.
ARRAY_NAME="HX Greenplum DW"

#### Naming convention for utility-generated data directories.
SEG_PREFIX=gpseg

#### Base number by which primary segment port numbers
#### are calculated.
PORT_BASE=40000

#### File system location(s) where primary segment data directories
#### will be created. The number of locations in the list dictate
#### the number of primary segments that will get created per
#### physical host (if multiple addresses for a host are listed in
#### the hostfile, the number of segments will be spread evenly across
#### the specified interface addresses).
declare -a DATA_DIRECTORY=(/data/gpdata/primary /data/gpdata/primary)

#### OS-configured hostname or IP address of the master host.
MASTER_HOSTNAME=node01

#### File system location where the master data directory
#### will be created.
MASTER_DIRECTORY=/data/gpdata/master

#### Port number for the master instance.
MASTER_PORT=5432

#### Shell utility used to connect to remote hosts.
TRUSTED_SHELL=ssh

#### Maximum log file segments between automatic WAL checkpoints.
CHECK_POINT_SEGMENTS=8

#### Default server-side character set encoding.
# FILE NAME: gpinitsystem_config

# Configuration file needed by the gpinitsystem

################################################
#### REQUIRED PARAMETERS
################################################

#### Name of this Greenplum system enclosed in quotes.
ARRAY_NAME="HX Greenplum DW"

#### Naming convention for utility-generated data directories.
SEG_PREFIX=gpseg

#### Base number by which primary segment port numbers
#### are calculated.
PORT_BASE=40000

#### File system location(s) where primary segment data directories
#### will be created. The number of locations in the list dictate
#### the number of primary segments that will get created per
#### physical host (if multiple addresses for a host are listed in
#### the hostfile, the number of segments will be spread evenly across
#### the specified interface addresses).
declare -a DATA_DIRECTORY=(/data/gpdata/primary /data/gpdata/primary)

#### OS-configured hostname or IP address of the master host.
MASTER_HOSTNAME=node01

#### File system location where the master data directory
#### will be created.
MASTER_DIRECTORY=/data/gpdata/master

#### Port number for the master instance.
MASTER_PORT=5432

#### Shell utility used to connect to remote hosts.
TRUSTED_SHELL=ssh

#### Maximum log file segments between automatic WAL checkpoints.
CHECK_POINT_SEGMENTS=8

#### Default server-side character set encoding.
ENCODING=UNICODE

################################################
#### OPTIONAL MIRROR PARAMETERS
################################################

#### Base number by which mirror segment port numbers
#### are calculated.
MIRROR_PORT_BASE=50000

#### Base number by which primary file replication port
#### numbers are calculated.
REPLICATION_PORT_BASE=41000

#### Base number by which mirror file replication port
#### numbers are calculated.
MIRROR_REPLICATION_PORT_BASE=51000

#### File system location(s) where mirror segment data directories
#### will be created. The number of mirror locations must equal the
#### number of primary locations as specified in the
#### DATA_DIRECTORY parameter.
declare -a MIRROR_DATA_DIRECTORY=(/data/gpdata/mirror /data/gpdata/mirror)


################################################
#### OTHER OPTIONAL PARAMETERS
################################################

#### Create a database of this name after initialization.
DATABASE_NAME=hx_gp

#### Specify the location of the host address file here instead of
#### with the the -h option of gpinitsystem.
MACHINE_LIST_FILE=/home/gpadmin/gpconfigs/hostfile_gpinitsystem
"gpconfigs/gpinitsystem_config" 78L, 2560C written     

3.11.初始化GP
[gpadmin@node01 ~]$ gpinitsystem -c /home/gpadmin/gpconfigs/gpinitsystem_config  -h /opt/gpinst/all_host

20170717:13:37:48:027877 gpinitsystem:node01:gpadmin-[INFO]:-Checking configuration parameters, please wait...
20170717:13:37:48:027877 gpinitsystem:node01:gpadmin-[INFO]:-Reading Greenplum configuration file /home/gpadmin/gpconfigs/gpinitsystem_config
20170717:13:37:48:027877 gpinitsystem:node01:gpadmin-[INFO]:-Locale has not been set in /home/gpadmin/gpconfigs/gpinitsystem_config, will set to default value
20170717:13:37:48:027877 gpinitsystem:node01:gpadmin-[INFO]:-Locale set to en_US.utf8
20170717:13:37:49:027877 gpinitsystem:node01:gpadmin-[INFO]:-MASTER_MAX_CONNECT not set, will set to default value 250
20170717:13:37:49:027877 gpinitsystem:node01:gpadmin-[INFO]:-Checking configuration parameters, Completed
20170717:13:37:49:027877 gpinitsystem:node01:gpadmin-[INFO]:-Commencing multi-home checks, please wait...
中间需要输入一次：Y
Continue with Greenplum creation Yy/Nn>
y
20170717:13:38:24:027877 gpinitsystem:node01:gpadmin-[INFO]:-Building the Master instance database, please wait...
如果没有报ERROR，GP数据库就安装好了。
查看数据库名称：hx_gp
 [gpadmin@node01 ~]$ psql -l
                  List of databases
   Name    |  Owner  | Encoding |  Access privileges
-----------+---------+----------+---------------------
 hx_gp     | gpadmin | UTF8     |
 postgres  | gpadmin | UTF8     |
 template0 | gpadmin | UTF8     | =c/gpadmin         
                                : gpadmin=CTc/gpadmin
 template1 | gpadmin | UTF8     | =c/gpadmin         
                                : gpadmin=CTc/gpadmin
(4 rows)

3.12 增加standby
一个gp集群只有一个master肯定会让人不放心，还好有备用，当master宕掉后，会自动启用standby作为master

在standby服务器上执行
[root@node02 ~]# mkdir /data1/gpdata/master
[root@node02 ~]# chown gpadmin:gpadmin /data1/gpdata/master

在master服务器上执行
[gpadmin@node01 ~]$ gpinitstandby -s node02
中间输入一次Y
20170717:16:29:14:025010 gpinitstandby:node01:gpadmin-[INFO]:-Validating environment and parameters for standby initialization...
20170717:16:29:14:025010 gpinitstandby:node01:gpadmin-[INFO]:-Checking for filespace directory /data/gpdata/master/gpseg-1 on node02
20170717:16:29:14:025010 gpinitstandby:node01:gpadmin-[INFO]:------------------------------------------------------
。。。。。。
。。。。。。
20170717:16:29:31:025010 gpinitstandby:node01:gpadmin-[INFO]:-Backup files of pg_hba.conf cleaned up successfully.
20170717:16:29:31:025010 gpinitstandby:node01:gpadmin-[INFO]:-Successfully created standby master on node02

 查看状态：gpstate

3.13增加mirror
mirror就是镜像，也叫数据备份。mirror对于数据存储来说很重要，因为我们的服务器指不定什么时候出毛病，有mirror就好很多了，因为两台存储节点同时宕掉的几率还是很小的。如果前面在GP初始化文件里忘记配置mirror了，请按照下面的方法添加
[gpadmin@node01 ~]$ gpaddmirrors -p 1000
运行过程中需要输入两次mirror路径：/data1/gpdata/mirror

3.14.设置访问权限
打开/data1/gpdata/master/gpseg-1/pg_hba.conf 按照最下面的格式添加客户端ip或网段
#user define
host    all     all     192.168.1.0/24   trust
host    all     all     127.0.0.1/28    trust

3.15.访问方式
可以通过gpAdmin桌面客户端来访问，也可以用命令行来访问，下面来说一下命令行访问的方式，loach是后面添加的用户
[gpadmin@node01 ~]$ psql -d hx_gp -h node01 -p 5432 -U gpadmin
[gpadmin@node01 ~]$ psql -d hx_gp -h node01 -p 5432 -U loach

3.16.创建用户
通过命令行登录以后，执行下面的命令
CREATE ROLE loach WITH LOGIN;
ALTER ROLE loach WITH PASSWORD 'loach';
