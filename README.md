# MyChat
一个基于itchat二次开发的私人微信小助手

## 环境
暂时只在Mac上测试运行。

## 运行
安装完所需要的python环境之后，运行main.py文件，扫描二维码之后登录微信至服务器正常运行即可。（）

## Component(目前可用的组件)

### Finder(文件管理器)

在移动端的微信中向文件传输助手输入以下命令：

1.获取终端初始化目录（默认是桌面目录）：
```
Dir init
```

2.进入目录电脑目录：
```
Dir cd [directory_name]
```

3.列出当前目录的下的目录和文件：
```
Dir ls
```

4.从电脑中传输文件：
```
Dir file [file_name]
```
