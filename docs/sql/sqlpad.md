# sqlpad
## 安装
- 安装nodejs
```
wget https://nodejs.org/dist/v9.3.0/node-v9.3.0-linux-x64.tar.xz
xz -d node-v9.3.0-linux-x64.tar.xz
tar -xf node-v9.3.0-linux-x64.tar
sudo ln -s /home/zhangxiwen/install/node-v9.3.0-linux-x64/bin/node /usr/bin/node
sudo ln -s /home/zhangxiwen/install/node-v9.3.0-linux-x64/bin/npm /usr/bin/npm

npm -v
```
```
sudo npm install sqlpad -g
#npm install -g npm
#运行
mkdir sqlpad
sqlpad --dbPath ../db --port 3010
sqlpad --help
```
- github源码安装
```
git clone https://github.com/rickbergfalk/sqlpad.git
cd sqlpad
scripts/build.sh
```
- docker安装
```
docker run --name sqlpad -d -p 5000:3000 skywidesoft/sqlpad:2.2.0
netstat -lnp | grep 5000
# 使用5000端口访问
```

## 访问
http://localhost:3010/
http://121.41.102.241:5000