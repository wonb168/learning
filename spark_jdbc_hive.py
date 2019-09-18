from pyspark.sql import SparkSession

jars='/opt/cloudera/parcels/CDH-5.15.0-1.cdh5.15.0.p0.21/lib/hive/lib/hive-jdbc-standalone.jar'
    # jars='/home/wang/MEGA/MEGAsync/jars/hive-jdbc-standalone.jar'
spark = SparkSession \
        .builder \
        .appName("hive") \
        .config("spark.driver.extraClassPath",jars) \
        .enableHiveSupport() \
        .getOrCreate()

def read_hive(url,dbtable):
    df = spark.read.jdbc(url=url, table=dbtable, properties=properties)
    return df

if __name__ == '__main__':
#   fire.Fire(Calculator)
       
    url="jdbc:hive2://192.168.*.*:10000"
    dbtable="(select * from wcz.test_orc) t" 
    properties={"user": "","password" : "","driver": "org.apache.hive.jdbc.HiveDriver"}
    df=read_hive(url,dbtable,properties)
