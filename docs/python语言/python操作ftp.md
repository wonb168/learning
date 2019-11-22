```
from ftplib import FTP

HOST = 'IP地址'
PORT=15021
USER = '用户名'
PASSWD = "密码"
image_dir="图片所在目录"

ftp=FTP()
ftp.connect(HOST,PORT)
ftp.login(user=USER, passwd=PASSWD)
ftp.cwd(image_dir)
ftp.dir('SSC6776BLK-*') #ftplib.error_perm: 550 SSC6776BLK-åæ¶.jpg: No such file or directory.
# 获取文件列表
print(ftp.size('SSC6776BLK.jpg'))
fs=ftp.nlst()
size=0
i=0
# 11324张图片，1224273782/(1024**3)=1.14G
for f in fs:
    if '-' not in f :# 排除乱码的，如SSC6776BLK-åæ¶.jpg
        size+=ftp.size(f)
        print(i)
        i+=1
   
print(size)

# 增量抓图片，获取图片的日期
ftp.sendcmd('MDTM SSC6776BLK.jpg')
```
得到结果： 213 20160311141800 ，str类型
实际文件日期是：2016/3/11 上午8:00:00
