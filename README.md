# win10_wallpaper_hook
save wallpapers of win10 to your own folders

保存windows10的壁纸到个人指定文件夹

## win10壁纸抓取器



### 调整配置文件configuration.ini

#### wallpaper_path
windows 10 自动下载壁纸的路径，通常为
```
C:/Users/<username>/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets
```

#### store_path
另存壁纸文件的主目录

#### desktop_wallpaper_dir
在另存壁纸主目录下，创建用于保存PC端壁纸的子目录名

#### mobile_wallpaper_dir
在另存壁纸主目录下，创建用于保存Mobile端壁纸的子目录名

### 调整main.bat脚本
修改cd /d 所在行，调整目录地址到main.py文件所在目录


### 配置后台自动运行

##### 1. 管理员权限账号登录

##### 2. 开始 - 程序 - windows 管理工具 - 任务计划程序

##### 3. 右键 - 新建任务

##### 4. 设置常规选项卡
* 设置为以 SYSTEM 用户运行
* 设置为不管用户是否登录都要运行
* 设置为以 SYSTEM 用户运行
* 设置为使用最高权限运行

##### 5. 设置触发器选项卡
* 设置触发器为 空闲状态

##### 6. 设置操作选项卡
* 指向本程序的main.bat文件

##### 7. 设置条件选项卡
* 勾选空闲部分的复选框：仅当计算机空闲时间超过下列值时才启动此任务，设置为10分钟

##### 8. 设置选项卡
目的是处理异常情况，勾选
* 如果任务运行时间超过以下时间，停止任务：1小时
* 如果请求后任务还在运行，强行将其停止



