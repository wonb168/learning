# pyspark

## 读取excel
```
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# 读excel
excel='/home/wang/Desktop/spark_excel.xlsx'
excel='file:///home/wang/Desktop/spark_excel.xlsx'#hadoop下file://

df = spark.read\
    .format("com.crealytics.spark.excel")\
    .option('location', excel)\
    .option("addColorColumns", "false")\
    .option("useHeader", "true")\
    .option("treatEmptyValuesAsNulls", "false")\
    .option("inferSchema", "true") \
    .option("timestampFormat", "MM-dd-yyyy HH:mm:ss")\
    .option("maxRowsInMemory", 20)\
    .option("excerptSize", 10)\
    .load()
df.printSchema()
df.show()
```