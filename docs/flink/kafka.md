# kafka安装
前提安装并配置jdk1.8，测试是否已安装
```
java -version
```
官网下载kafka安装包，解压：

```
./zookeeper-server-start.sh ../config/zookeeper.properties

./kafka-server-start.sh ../config/server.properties
```



# kafka使用

1. 创建kafka主题：


```shell
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
```

2. 显示kafka所有主题：
```shell
bin/kafka-topics.sh -list -zookeeper localhost:2181
```


3. 创建kafka生产者：
```shell
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
```

​	输入hello world

4. 创建kafka消费者：
```shell
bin/kafka-console-consumer.sh --zookeeper改 localhost:2181 --topic test --from-beginning
#新版--zookeeper改--bootstrap-server
#从第一条开始接受
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning  
```

​	接收到hello world

# kafka读rdb
## 启动kafka（先zookeeper）

```shell
cd /home/wang/Downloads/kafka_2.12-2.4.0/bin/
./zookeeper-server-start.sh ../config/zookeeper.properties
./kafka-server-start.sh ../config/server.properties
```
## oracle配置
- oracle的jdbc驱动jar,放在kafka的安装包下的lib目录
- 下载的connect插件解压后的Lib下的jar包都放在plugin.path目录
修改connect-standalone.properties，添加
```
plugin.path=/home/wang/Downloads/kafka_2.12-2.4.0/share/java
```
新增oracle配置文件，内容如下：
oracle内部表名和列名都是大写，所以配置中table.whitelist和incrementing.column.name都要大写
```
name=test-oracle-connector
connector.class=io.confluent.connect.jdbc.JdbcSourceConnector
tasks.max=1
connection.password=dev
connection.url=jdbc:oracle:thin:@192.168.16.235:1521:orcl
connection.user=dev
table.whitelist=TEST_DATE
mode=incrementing
incrementing.column.name=ID
topic.prefix=test-oracle-
```
## 从oracle取数
1. 启动connector
```
./connect-standalone.sh ../config/connect-standalone.properties ../config/from-oracle.properties
```
2. 启动consumer
```
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic test-oracle-TEST_DATE
```
## 从sqlserver取数
1. 启动connector
```
./connect-standalone.sh ../config/connect-standalone.properties ../config/from-sqlserver.properties 
```
显示主题
```
./kafka-topics.sh -list -zookeeper localhost:2181
```
需添加schema，但如果2个schema都有同名表咋搞？？
```
schema.pattern=dbo
table.whitelist=test
```
https://stackoverflow.com/questions/55750710/how-to-use-the-kafka-connect-jdbc-to-source-postgresql-with-multiple-schemas-tha
2. 启动consumer
```
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic test-sqlserver-dbo.test
```