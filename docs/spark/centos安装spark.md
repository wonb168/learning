# centos7安装spark
## 下载
1. java1.8
```
#centos7
yum -y install java-1.8.0-openjdk java-1.8.0-openjdk-devel
dirname $(readlink $(readlink $(which java)))
  
vim /etc/profile
```
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.232.b09-0.el7_7.x86_64/
#上面dirname命令获取到的路径，不要jre/bin最后这段
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar

测试：
```
source /etc/profile
java -version
```

2. scala
```
axel -n 50 https://downloads.lightbend.com/scala/2.12.2/scala-2.12.2.tgz
tar xzvf scala-2.12.2.tgz

sudo vim /etc/profile
```

export SCALA_HOME=/usr/local/scala-2.12.4
export PATH=${JAVA_HOME}/bin:${SCALA_HOME}/bin:$PATH

3. spark
http://spark.apache.org/下载spark-2.4.4-bin-hadoop2.6.tgz
```
# 解压
tar xzvf spark-2.4.4-bin-hadoop2.6.tgz
```
## 环境变量配置
```
export JAVA_HOME=/usr/local/java/jdk1.8.0_221
export CLASSPATH=.:${JAVA_HOME}/lib:${JAVA_HOME}/jre/lib
export SCALA_HOME=/opt/scala/scala-2.12.2
export SPARK_HOME=/opt/spark/spark-2.4.3-bin-hadoop2.7
export PATH=${JAVA_HOME}/bin:${SPARK_HOME}/bin:${SCALA_HOME}/bin:$PATH
```
