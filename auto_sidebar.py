# encoding:utf-8

import os
 
 
def get_filelist(path): 
    print('path:',path)
    txt = ["* [首页](/)"]
    # os.system("echo '* [首页](/)' > "+path+"/_sidebar.md")
    # os.system("> "+path+"/_sidebar.md")
    for home, dirs, files in os.walk(path): 
        print('home:',home)
        print('dirs:',dirs)
        print('files:',files)
        if home==path:
            txt="* [首页](/)"
        elif not home.endswith('assets'):    
            print('path,home:',path,home)
            pathname=home.replace(path+"\\","")
            print('pathname:',pathname)
            txt=txt+"\n* ["+pathname+"]("+pathname+"/)"
            # txt=txt+"\n* ["+pathname+"]"
        for filename in files: 
            # 文件名列表，包含完整路径 
            # md
            if ".md" in filename and not filename.startswith("_") and not filename.startswith("README"):
                filename=filename.replace(".md","")
                # print("filename:",filename)
                txt=txt+"\n    * ["+filename+"]("+pathname+"/"+filename+")"
        # print(txt)
    # return Filelist
    with open(path+"/_sidebar.md", 'w',encoding='utf-8') as f:
        f.write(txt)

if __name__ =="__main__":
    # print(os.getcwd())
    path=os.path.abspath(os.path.dirname(__file__))
    print(path)#当前py文件所在路径
    path =path+'/docs'
    Filelist = get_filelist(path) 
    
"""
* [首页](/)
* [flink](flink/)
    * [flink安装](flink/flink安装)
    * [kafka](flink/kafka)
* [kettle](kettle/)
    * [web运行与监控carte](kettle/web运行与监控carte)

* [首页](/)
* [sql](sql/)
    * [sql经典问题](sql/sql经典问题)
    * [postgre常用](sql/postgre常用)
    * [oracle常用](sql/oracle常用)
    * [sqlserver常用](sql/sqlserver常用)
* [linux](linux/)
    * [scp用法](linux/scp)
    * [gp集群](linux/gp集群)
* [windows](windows/)
    * [批量修改图片大小](windows/批量修改图片大小)
* [工具](tools/)
    * [常用软件](tools/software)
"""