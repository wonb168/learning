from pyspark.sql import SparkSession

host='192.168.16.235'
port=1521
dbname='orcl'
url="jdbc:oracle:thin:@{}:{}/{}".format(host, port, dbname)
user='system'
password='123456'
driver='oracle.jdbc.OracleDriver'

spark = SparkSession \
    .builder \
    .appName("spark") \
    .config("hive.metastore.uris", "thrift://192.168.200.101:9083") \
    .enableHiveSupport() \
    .getOrCreate()
dbtable='bi.pyspark_etl'
df=spark.read.format("jdbc").options(url=url,
    driver=driver,
    dbtable=dbtable,
    user=user,
    password=password).load()

df.printSchema()

#写hive
df.write.saveAsTable("wcz.test_oracle")
# df.coalesce(1)
#     .write()
#     .mode(SaveMode.Append)
#     .format("parquet")
#     .partitionBy("year")
#     .saveAsTable("tblclick8partitioned");
