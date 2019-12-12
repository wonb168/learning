# 总体设计
## 目标
1. 近期目标：ods、edw零编码，airflow自动化
2. 中期目标：去掉开发环境（只需测试、生产）
3. 远期目标：干掉etl工程师

1. 选字段时加翻页/滚动
2. 代码的提示
3. 租户-项目-作业
4. 与git打通

## 功能设计
1. 直连数据库，通过选择的方式来映射，确保准确性
2. 特殊情形允许自定义sql，方便工具自动生成etl脚本
3. 作为SaaS服务提供，多租户设计
4. 支持在工具内进行sql查询
## 页面校验
1. 多张来源表时，没有孤立的表（一定要有关联关系）
2. 必选字段必选有填写
3. 多张表时必须有一张主表

##左侧目录树查询
代码优化，不显示没有权限的表。（几乎所有的客户端都显示所有库、表，等点击展开时才告知没权限）

### oracle
```
-- 有权限的库表(含视图)
select * from user_tab_privs; # 用户表
-- 表的所有字段(含视图)
select OWNER,TABLE_NAME,A.COLUMN_NAME,A.DATA_TYPE  
rom user_tab_columns A
where TABLE_NAME='表名' and OWNER='用户'
order by A.COLUMN_ID asc
```
### sqlserver
https://blog.csdn.net/zhenglianghui163/article/details/79013375
```
-- 有权限的库表（如果获取库名、schema名）
SELECT * FROM INFORMATION_SCHEMA.TABLES #推荐，库-schema-表
SELECT * FROM INFORMATION_SCHEMA.VIEWS
select * from sysobjects where xtype in('U','V') #表和视图

-- 表的所有字段（含视图）
select * from syscolumns where id=OBJECT_id('d_Retail') order by colid

```