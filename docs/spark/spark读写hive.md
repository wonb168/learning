
```
from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("spark") \
    .config("hive.metastore.uris", "thrift://192.168.200.101:9083") \
    .enableHiveSupport() \
    .getOrCreate()

df=spark.sql('desc table jdv_edw_dev.fct_sales')
df.show()
df.createOrReplaceTempView('tmp')
sql="""
select 'edw' as schema_name,'fct_sales' as table_name, col_name as column_name,1 as is_required,comment as column_comment 
from tmp where col_name not like '# Partition%'
"""
df2=spark.sql(sql)
# jdbc url
url = "jdbc:postgresql://192.168.200.201:5432/autoetl"
table='web.target_table'
mode='append'

# JDBC参数字典
properties = {
    "user": "autoetl",
    "password": "密码",
    "driver": "org.postgresql.Driver"
}

# DataFrame.write.jdbc
df2.write.jdbc(url=url, table=table, mode=mode, properties=properties)
```
## dataframe添加序号
```
// 在原Schema信息的基础上添加一列 “id”信息
val schema: StructType = dataframe.schema.add(StructField("id", LongType))

// DataFrame转RDD 然后调用 zipWithIndex
val dfRDD: RDD[(Row, Long)] = dataframe.rdd.zipWithIndex()

val rowRDD: RDD[Row] = dfRDD.map(tp => Row.merge(tp._1, Row(tp._2)))
// 将添加了索引的RDD 转化为DataFrame
val df2 = spark.createDataFrame(rowRDD, schema)
df2.show()
```

