## 下载
```
wget https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
wget https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-sqlplus-19.6.0.0.0-1.x86_64.rpm
wget https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-devel-19.6.0.0.0-1.x86_64.rpm
```
## 安装
```
rpm -ivh *.prm
```
## 配置
```
mkdir -p /usr/lib/oracle/11.2/client64/network/admin

vim /usr/lib/oracle/11.2/client64/network/admin/tnsnames.ora

ORACLE_URL  =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.1.59)(PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = TPSI)
    )
  )

vi ~/.bashrc

export  ORACLE_HOME=/usr/lib/oracle/11.2/client64
export  ORACLE_HOME=/home/kailan_dev
export  TNS_ADMIN=$ORACLE_HOME/network/admin
export  LD_LIBRARY_PATH=$ORACLE_HOME/lib 
export  PATH=$ORACLE_HOME/bin:$PATH
export  NLS_LANG=AMERICAN_AMERICA.ZHS16GBK
————————————————

原文链接：https://blog.csdn.net/chengyuqiang/article/details/80406159
```
## 运行
```
sqlplus
sqlplus LENLELZ/LZ123@//192.168.1.59:1521/ORACLE_URL 
sqlplus LENLELZ/LZ123@//192.168.18.2:1521/ORACLE_URL 
sqlplus scott/tiger@192.168.1.123:1521/orcl
sqlplus LENLELZ/LZ123@192.168.18.2:1521/ORACLE_URL 
sqlplus LENLELZ/LZ123@192.168.18.2:1521/TPSI

pyspark  --jars "/opt/spark_cli/driver/ojdbc6.jar" 
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:oracle:thin:@//192.168.1.59:1521/TPSI") \
    .option("dbtable", "LENLEINTERFACE.VLZ_DIM_SKU") \
    .option("user", "LENLELZ") \
    .option("password", "LZ123") \
    .option("driver", "oracle.jdbc.driver.OracleDriver") \
    .load()

```

source /opt/spark_code/env.sh; /opt/spark_cli/spark-2.4.2-bin-hadoop2.7/bin/spark-submit --jars "/opt/spark_cli/driver/ojdbc6.jar"  --conf spark.driver.host=192.168.18.2  --conf spark.driver.port=4040  --master yarn --deploy-mode cluster  --num-executors 10 --executor-memory 4G --executor-cores 4 --driver-memory 8G --conf spark.default.parallelism=1000 --conf spark.storage.memoryFraction=0.5  --conf spark.shuffle.memoryFraction=0.3 --queue etl  /opt/spark_code/kailan_ods/p_ods_dim_sku_dev.py 2020-05-08
ssh -g -L 1521:192.168.1.59:1521 localhost
netstat -lnp|grep 1521
ps -fe|grep 1521

ALTER TABLE ods.vlz_dim_sku ADD COLUMNS (min_order_qty string)
ALTER TABLE ods.vlz_dim_sku CHANGE min_order_qty min_order_qty string after spec;
alter table table_name add columns (c_time string comment '当前时间'); -- 正确，添加在最后
alter table table_name change c_time c_time string after address ;
ALTER TABLE ods.vlz_dim_sku RENAME TO ods.vlz_dim_sku_old;
ALTER TABLE ods.vlz_dim_sku2 RENAME TO ods.vlz_dim_sku;

ALTER TABLE edw.dim_sku ADD COLUMNS (spec decimal(18,6),min_order_qty string);
ALTER TABLE edw_ai.dim_sku ADD COLUMNS (spec decimal(18,6),min_order_qty string);

  