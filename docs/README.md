# 我的博客是怎么炼成的？——振振有CI
一起都想弄个自己的博客，想想需要制作网页（即使有博客框架、模板也挺复杂），最关键还得有外网服务器进行部署，就打住了。
直到发现了docsify+github这对“黄金搭档”。
1. docsify： 实时渲染markdown文件为html
2. github：  github page可以将你的git工程发布为个人网页

## docsify安装配置
```
# 安装
npm i docsify-cli -g
# 初始化
docsify init ./docs
```

初始化成功后，可以看到 ./docs 目录下创建的几个文件：
index.html 入口文件
README.md 会做为主页内容渲染
.nojekyll 用于阻止 GitHub Pages 会忽略掉下划线开头的文件

直接编辑 docs/README.md 就能更新网站内容，但博客不可能所有内容写在一个md文件中。

## docsify多页面制作
需要在index.html文件中的window.$docsify中开启loadSidebar选项：
```
<script>
  window.$docsify = {
    loadSidebar: true
  }
</script>
<script src="//unpkg.com/docsify"></script>
```
然后在根目录创建自己的_sidebar.md文件，配置我们需要显示的页面。
比如我的【侧边栏】导航_sidebar.md文件：
```
* [首页]（/)
* [linux](linux/)
    * [scp用法](linux/scp)
* [工具](tools/)
    * [常用软件](tools/software)
```

## 本地预览
```
docsify serve
``` 
通过 http://localhost:3000访问。LiveReload 功能，md修改可以实时预览。

## github发布
将docs目录放到一个github工程中，进入该工程的setting：
GitHub Pages 支持从三个地方读取文件：
docs/ 目录
master 分支
gh-pages 分支
开启 GitHub Pages 功能并选择 master branch /docs folder 选项。
发布成功后会显示网站地址，通过这个地址即可在线访问你编写的技术文档了。
