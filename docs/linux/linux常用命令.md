
# linux常用命令
## scp上传、下载文件
	• 从远程将文件拷回本地
	scp –用户名@计算机IP或者计算机名称:文件名 本地路径
```    
scp -P 44422 root@114.55.33.101:/mnt/mysql/mysql/sanlux/MF_POS.* /var/lib/mysql 
```
## 上传密钥
```
ssh-copy-id -i ~/.ssh/id_rsa.pub -p 22 zhangxiwen@121.41.102.241
```