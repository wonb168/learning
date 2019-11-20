# raise用法
raise用于函数中打印输出，类似于oracle的dbms_output.putline();
raise的语法为：
```
raise notice 'this is raise test %',param;
```
上面语句中的%为参数占位符，有多个参数时就添加多个%，不用考虑参数的数值类型；notice字段为级别，可以为debug/log/info/notice/warning/exception，这些级别的信息是直接写到服务端日志还是返回到客户端或是二者皆有，是由log_min_messages和client_min_messages两个参数控制，这两个参数在数据库初始化时用到。