# encoding:utf-8

import os
 
 
def get_filelist(path): 
    print(path)
    Filelist = ["* [首页](/)"]
    # os.system("echo '* [首页](/)' > "+path+"/_sidebar.md")
    os.system("> "+path+"/_sidebar.md")
    for home, dirs, files in os.walk(path): 
        if home==path:
            txt="* [首页](/)"
        else:    
            pathname=home.replace(path+"/","")
            # txt="* ["+pathname+"]("+pathname+"/)"
            txt="* ["+pathname+"]"
        cmd="echo '"+txt+"' >> "+path+"/_sidebar.md"
        os.system(cmd)
        for filename in files: 
            # print(home)
            # print(dirs)
            # print(files)
            # 文件名列表，包含完整路径 
            # md
            if ".md" in filename and not filename.startswith("_") and not filename.startswith("README"):
                filename=filename.replace(".md","")
                # print("filename:",filename)
                txt="* ["+filename+"]("+pathname+"/"+filename+")"
                cmd="echo '    "+txt+"' >> "+path+"/_sidebar.md"
                os.system(cmd)
                # Filelist.append(txt)
            # Filelist.append(os.path.join(home, filename))
            # Filelist.append(filename)
            # # 文件名列表，只包含文件名
            # Filelist.append( filename)
    return Filelist

if __name__ =="__main__":
    # print(os.getcwd())
    path=os.path.abspath(os.path.dirname(__file__))
    print(path)#当前py文件所在路径
    path =path+'/docs'
    Filelist = get_filelist(path) 
    print(len( Filelist)) 
    # for file in  Filelist : 
    #     print(file)
    # cmd="echo "+Filelist+" > "+path+"/_sidebar.md"
    # print("cmd:",cmd)
    # os.system(cmd)
"""
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