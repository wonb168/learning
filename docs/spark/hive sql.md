# 滚动删除3个月分区数据
hive -e "alter table table_name drop partition(partition_name<'`date -d "3 month ago" +"%Y-%m-%d"`')"