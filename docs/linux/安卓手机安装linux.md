1. 安装termux
兔兔助手app里下载termux
termux 上的 sshd 不能通过 IP 连接, 只能使用密钥,
termux 预装了 telnetd, 只需要输入 telnetd 即可在 8023 端口开启服务
```
--查手机IP
wifi里看
--pc登录
telnet 192.168.20.3 8023
```
2. 安装arch
```
--git方式（安装时报错）
pkg install git
git clone https://github.com/sdrausty/TermuxArch
--下载完成代码后，开始启动安装
bash TermuxArch/setupTermuxArch.sh
-- wget方式（ok）
pkg install wget
wget https://sdrausty.github.io/TermuxArch/setupTermuxArch.sh
bash setupTermuxArch.sh
```
经过漫长的等待，安装好了，输入```startarch```就可以使用了　　

链接：https://www.jianshu.com/p/0f0c2bd29a50