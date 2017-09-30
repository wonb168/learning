导出表结构：-s -t
pg_dump -s -t xxxx.tbtest testdb > tbnode.out
/usr/local/greenplum-db-4.3.14.1/bin/pg_dump -s -t -h localhost -U gpadmin bigdata > /gp/pg.bak

导出表结构和内容：-t
pg_dump -h mdw -t xxxx.tbtest testdb > tbnode.sql

只导出某个表的内容：-a
pg_dump -h mdw -t xxxx.tbtest -a testdb > tbnode.sql
pg_restore
pg_restore用于恢复pg_dump导出的非纯文本格式备份。pg_dump默认是-Ft（plain text）参数，也就是纯文本备份。

参数：
-F, --format=c|t|p       output file format (custom, tar, plain text)

纯文本备份（-Ft）使用pg_restore会报错，如下
$ pg_dump -t member -Uszlsd -W szlsd_db -f /gpbackup/member.dmp

$ pg_restore -d szlsd_db /gpbackup/member.dmp
pg_restore: [archiver] input file does not appear to be a valid archive


当pg_dump时使用-Fc或者-Ft，就可以利用pg_restore进行恢复
$ pg_dump -t member -Fc -Uszlsd -W szlsd_db -f /gpbackup/member_c.dmp

$ pg_restore -d szlsd_db /gpbackup/member_c.dmp
上传文件
scp /gp/gpback.bak root@192.168.251.93:/data/gpadmin/
