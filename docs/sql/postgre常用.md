# raise用法
raise用于函数中打印输出，类似于oracle的dbms_output.putline();
raise的语法为：
```
raise notice 'this is raise test %',param;
```
上面语句中的%为参数占位符，有多个参数时就添加多个%，不用考虑参数的数值类型；notice字段为级别，可以为debug/log/info/notice/warning/exception，这些级别的信息是直接写到服务端日志还是返回到客户端或是二者皆有，是由log_min_messages和client_min_messages两个参数控制，这两个参数在数据库初始化时用到。
## 关联更新
```
--参照一张表
update obj_table a 
set code=b.code --注意左边的code不能加别名
from ref_table b 
where a.id=b.id 
;
--参照多张表（或先bc关联为临时表再用上面的方式）
update a
set value = c.value
from b,c
where a.b_id = b.id
    and b.c_id = c.id
    and a.key = 'test'
;

```
# filter过滤
```
--filter函数
select stu_id, count(*), count(*) filter (where score<60) as "不及格"
from sherry.agg_filter
group by stu_id 

--使用case when
select stu_id, count(*), sum(case when score<60 then 1 else 0) as "不及格"
from sherry.agg_filter group by stu_id
```