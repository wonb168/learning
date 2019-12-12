# oracle sql
## 所有有权限的库表
```
select * from dba_tab_privs;
select * from all_tab_privs;
select * from user_tab_privs; -- 用户表
```
# 元数据查询
## 创建只能访问其他用户表的用户
```
--创建用户zhangsan 密码123456

create user test identified by test; 
--给用户赋权限（只能登录的权限）

grant create session to test;
--登录要被访问表的用户，执行

select 'GRANT SELECT ON '||owner||'.'||table_name||' to dev ;'--select *
from all_tables where owner='BI'

## 查用户下所有表 
```
select * from all_tables where owner='BI'
select table_name from user_tables;
```

将SYS用户的口令修改成123456后，可按以下几种方法登录：

法1.sqlplus / as sysdba 【以操作系统认证的方式登录，不需要用户名和口令】

法2.sqlplus sys/abcde as sysdba;

法3.sqlplus sys/ as sysdba