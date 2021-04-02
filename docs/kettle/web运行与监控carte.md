更方便，不用登录服务器执行和监控运行状态。

更快速，命令行运行有几分钟不等的启动及初始化时间。

1. 开启carte服务

```
nohup ./carte.sh 192.168.1.240 9999 &
```

2. 运行转换 executeTrans

```
## 资源库形式（资源库、文件皆可,不需ktr后缀）
curl -u "cluster:cluster" "http://192.168.1.240:9999/kettle/executeTrans/?rep=kettle_hsty&trans=/dim_skc_test"
## 文件形式
curl -u "cluster:cluster" "http://192.168.1.240:9999/kettle/executeTrans/?trans=/data/kettle/data-integration/edw_ai/dim_skc_test.ktr&testvar=abc"
```

   亦可**chrome安装rested、restman等api插件运行url**部分。传参get和post形式皆可。

3. 运行作业executeJob

```
curl -u "cluster:cluster" "http://192.168.1.240:9999/kettle/executeJob/?rep=kettle_hsty&job=/test_job&P1=test"
## post传参
http://192.168.1.240:9999/kettle/executeJob/?job =/opt/pentaho/INSERT_VALUTA.kjb --post-data" VALUTA_DATE = 2019-08-08＆TYPE = 1＆MORE = XYZ"

```

4.查看任务状态

   浏览器访问：192.168.1.240:9999