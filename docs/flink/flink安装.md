# manjaro安装flink

## 下载

```shell
#下载
axel -n 10 http://mirrors.tuna.tsinghua.edu.cn/apache/flink/flink-1.9.1/flink-1.9.1-bin-scala_2.12.tgz
#解压
sudo tar -zxf flink-1.9.1-bin-scala_2.12.tgz -C /usr/local
```

```shell
cd /usr/local
sudo mv ./flink-*/ ./flink
sudo chown -R hadoop:hadoop ./flink #此步未执行
```

## 修改配置文件

- `Flink`对于本地模式是开箱即用的，如果要修改Java运行环境，可修改`conf/flink-conf.yaml`中的`env.java.home`，设置为本地java的绝对路径

### 添加环境变量



```shell
vim ~/.bashrc
export FLNK_HOME=/usr/local/flink
export PATH=$FLINK_HOME/bin:$PATH
```
```
vim  conf/flink-conf.yaml
```


## 启动Flink



```shell
start-cluster.sh
```

- 可以通过观察logs目录下的日志来检测系统是否正在运行了
或```jps```测试

```shell
tail log/flink--jobmanager-.log #未找到此log
```



JobManager同时会在8081端口上启动一个web前端，通过[http://localhost:8081](http://localhost:8081/)来访问
```
./bin/flink run ./examples/batch/WordCount.jar #ok
./bin/flink run ./examples/streaming/SocketWindowWordCount.jar --port 8000 #not ok
```

