# spark读写数据库
## jar包
1. 放到spark的jars目录：
spark-2.4.4-bin-hadoop2.6/jars/ojdbc6.jar
2. 提交应用程序或启动shell时，带JDBC驱动程序。

```
bin/pyspark --packages group:name:version  
#或者组合driver-class-path和jar
bin/pyspark --driver-class-path $PATH_TO_DRIVER_JAR --jars $PATH_TO_DRIVER_JAR
```
也可以在JVM实例启动之前使用PYSPARK_SUBMIT_ARGS环境变量设置这些属性，
或者使用conf/spark-defaults.conf设置spark.jars.packages或spark.jars / spark.driver.extraClassPath。

## 读jdbc库

```
spark.read.jdbc(url=url, table="baz", properties=properties)
```
## 写jdbc库
Spark JDBC writer支持以下模式：

- append: Append contents of this DataFrame to existing data.
- overwrite: Overwrite existing data.
- ignore: Silently ignore this operation if data already exists.
- error (default case): Throw an exception if data already exists.

```
# jdbc url
url = "jdbc:postgresql://localhost/foobar"

# JDBC参数字典
properties = {
    "user": "foo",
    "password": "bar"，
    "driver": "org.postgresql.Driver"
}

# DataFrame.write.jdbc
df.write.jdbc(url=url, table="baz", mode=mode, properties=properties)
```