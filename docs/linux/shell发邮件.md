centos7 shell mail发送邮件

# centos7 mail发送邮件
```
#安装sendmail
yum  -y  install  sendmail
systemctl  start  sendmail
 
#安装mailx
yum install -y mailx
 
#配置文件
vim /etc/mail.rc

set ssl-verify=ignore
set nss-config-dir=/etc/pki/nssdb
set from=etl@linezonedata.com 
set smtp=smtps://smtp.exmail.qq.com:465
set smtp-auth-user=etl@linezonedata.com
set smtp-auth-password=密码
set smtp-auth=login
```
set nss-config-dir=/etc/pki/nssdb#使用命令find / -name "cert*.db" 查找位置（根据自身系统而定）
接收服务器：
imap.exmail.qq.com(使用SSL，端口号993)
发送服务器：
smtp.exmail.qq.com(使用SSL，端口号465)
腾讯企业邮箱配置文件
```shell
##exmail：
##邮箱地址
set from=etl@linezonedata.com
##smtp服务器
set smtp="smtps://smtp.exmail.qq.com:465"
##用户名
set smtp-auth-user=etl@linezonedata.com
##密码
set smtp-auth-password=密码
set smtp-auth=login
##使用SSL的方式发送邮件
set smtp-user-starttls
set ssl-verify=ignore
#ssl.crt地址
set nss-config-dir=/etc/mail.rc_ssl.crt
```
原文：https://blog.csdn.net/t_Aier/article/details/80637377 

# 发邮件
manjaro设置
vim ~/.mailrc
/home/wang/.pki/nssdb/cert9.db
```
echo "这是邮件内容" | mailx -v -s "这是邮件标题" wangchangzhen@linezonedata.com,wangchangzhen@linezonedata.com <这是附件-调度日志.log
#直接附件
echo "这里输入你邮件内容" | mailx -s "邮件标题" -a file.txt wangchangzhen@linezonedata.com

#强制附件
echo "这里输入你邮件内容" | mail -s "邮件标题" -a file.txt wangchangzhen@linezonedata.com 
Cannot start /usr/sbin/sendmail
```

