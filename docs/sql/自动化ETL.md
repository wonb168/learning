# 左侧目录树查询
代码优化，不显示没有权限的表。（几乎所有的客户端都显示所有库、表，等点击展开时才告知没权限）

## oracle
```
-- 有权限的库表(含视图)
select * from user_tab_privs; # 用户表
-- 表的所有字段(含视图)
select OWNER,TABLE_NAME,A.COLUMN_NAME,A.DATA_TYPE  
rom user_tab_columns A
where TABLE_NAME='表名' and OWNER='用户'
order by A.COLUMN_ID asc
```
## sqlserver
https://blog.csdn.net/zhenglianghui163/article/details/79013375
```
-- 有权限的库表（如果获取库名、schema名）
SELECT * FROM INFORMATION_SCHEMA.TABLES #推荐，库-schema-表
SELECT * FROM INFORMATION_SCHEMA.VIEWS
select * from sysobjects where xtype in('U','V') #表和视图

-- 表的所有字段（含视图）
select * from syscolumns where id=OBJECT_id('d_Retail') order by colid

```