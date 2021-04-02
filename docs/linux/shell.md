## 文件日期
```

ls -l |awk '$9 ~ /'$pattern'/ {\
     ctime="date -d \""$6" "$7" "$8"\" +%Y%m%d%H%M"; \
     ctime|getline filetime; if( filetime > '$checktime' ) print $9 ; }

ls -l --time-style=long-iso|awk '{ctime="date -d \""$4"\" +%Y%-m%-d%"; ctime|getline $4; if( $4 > '2019-11-11' ) print $4" "$6 ; }'
# 列出光棍节后的jpg文件
ls -l --time-style=long-iso|awk '$6 ~ /'.jpg'/{if( $4 > '2019-11-11' ) print $6 ; }'


# 30天前
hadoop fs -ls --time-style=long-iso | awk 'BEGIN{ days_ago=strftime("%F", systime()-30*24*3600) }{ if($4<"days_ago"){printf "%s\n", $6} }' #例子


date -d "10 day ago 2019-07-16" +%Y%m%d
```
1、临时更改显示样式，当回话结束后恢复原来的样式
    export TIME_STYLE='+%Y-%m-%d %H:%M:%S'    # 直接在命令中执行即可

2、永久改变显示样式，更改后的效果会保存下来
    修改/etc/profile文件，在文件内容末尾加入
    export TIME_STYLE='+%Y-%m-%d %H:%M:%S'

    执行如下命令，使你修改后的/etc/profile文件配置内容生效
    source /etc/profile