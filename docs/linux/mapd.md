# cuda安装
检测是否英伟达显卡
 lspci | grep -i nvidia
## lspci安装
在CentOS的最小化安装中，默认是不会安装lspci工具的，需要自己手动安装。
     安装步骤：1、yum  whatprovides  */lspci  /*查找lspci是通过哪个安装包来提供的
               2、yum install pciutils
wget http://www.kernel.org/pub/software/utils/pciutils/pciutils-3.1.4.tar.bz2
tar -xvjf pciutils-3.1.4.tar.bz2

# cuda安装
检查是否有正确的kernel headers
https://docs.ucloud.cn/ai/gpu/operation/centos7_cuda
## mapd安装
