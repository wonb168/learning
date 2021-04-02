https://www.jianshu.com/p/09a3bbb8b362
# markdown做ppt
## ppt-cli

1. 安装 node,ppt-cli
```
npm install -g ppt-cli
```
2. 播放ppt
```
ppt sample.md
ppt sample.md --align=center --theme=black --transition=zoom
#也可以直接使用线上的 markdown 文件
ppt https://raw.githubusercontent.com/jirengu/server-mock/master/README.md
```

## marp 
md文件头部添加：
```
---
marp: true
---
```
## reveal.js 
