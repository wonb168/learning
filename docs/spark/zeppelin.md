# 简介
Apache Zeppelin提供了web版的类似ipython的notebook，用于做数据分析和可视化。背后可以接入不同的数据处理引擎，包括spark, hive, tajo等，原生支持scala, java, hell, markdown等。一个基于web的笔记本，支持交互式数据分析。你可以用SQL、Scala等做出数据驱动的、交互、协作的文档。(类似于ipython notebook，可以直接在浏览器中代码、笔记并共享)
# 安装
下载地址：http://zeppelin.apache.org/download.html
```
tar -zxvf zeppelin-0.8.0-bin-all.tgz
# 替换jar包（重点！！！）
spark下的jackson-*.jar和netty-*.jar替换lib目录下的
连hive需将hive-site.xml复制到conf目录下
# 启动
bin/zeppelin-daemon.sh start #win下用zeppelin.cmd启动

```
# 使用
登录：localhost:8080
