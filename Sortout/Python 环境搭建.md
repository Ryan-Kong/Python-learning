# 在Mac上使用Python3
##### 搭建环境: 
自己的电脑很老，Early 09 的 iMac 20-inch（OS High Sierra 10.13.3）  
【image】  
升级到High Sierra 也是自己通过教程升级来的  
教程地址：

进入正题，由于Mac默认自带Python2.7版本，学习最新的Python3的话，但也不能直接放弃2.7是不，所以最好的方式就是保留两个版本，双版本的话推荐的方式就是————Homebrew
主要过程就几步： 

- Step 1 安裝 Xcode
- Step 2 安裝套件管理工具 Homebrew
- Step 3 安裝 Python
- Step 4 設定路徑 $PATH（不跟系統 Python 打架）
- Step 5 最后的设置

####Setp 1 安装Xcode
可以到 App Store 搜尋 Xcode 並安裝即可  
装好需要运行下Xcode，**同意License Agreement**
我的版本会同时配置好Xcode command line tool，如果没有的话就需要到 terminal 手动輸入來安裝

        xcode-select --install
#### Step 2 安装Homebrew
Homebrew是Mac的一款套件管理工具，本人小白跟着官网【官网链接】的教程走即可

        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
安装好之后，运行下
        
        brew doctoc

来确认下，系统报错的话根据提示操作即可。

#### Step 3 安装Python3
系统已经有Python2的情况下，我就直接进入安装Python3的过程
代码也很简单：

        brew install python3

>教程这里不知道有什么用？
Pthon3 会被安装在 /usr/local/Cellar 下 

#### Step 4 配置PATH
为了不让不同版本Python打架，还需要配置PATH，完全根据教程来即可

>什麼是路徑 $PATH 呢？  
還記得我們在裝 Python 的時候，輸入了 brew，  
系統就自動會知道要開始跑 homebrew。  
系統到底怎麼知道我們的 brew 在哪裡？  
這就是 $PATH 的用途了！    
``` echo $PATH ```  
接下來就會看到一串類似這樣的東西  
```/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin```  
分號 (:) 是分隔的意思  
所以當你在 terminal 裡面輸入 brew 時  
系統就會開始從 /usr/bin 找起  
如果在 /usr/bin 裡面找不到的話  
就會往下一個 /bin 去搜尋，以此類推  
brew 其實就在 /usr/local/bin 裡面！  
所以現在的問題就是，系統在 /usr/bin 裡面也有一份 Python  
現在我們在 /usr/local/Cellar 裡面也裝了 Python  
這樣在 terminal 打上 python 指令時，誰會被開啟呢？  
因為路徑有順序，所以它會先找到系統的 Python  
現在就要來解決這個問題  
```sudo vi /etc/paths```  
現在要把 /usr/local/bin 移到上面去   
【images】   
```:wq```  
退出保存

#### Step 5 大功告成？还有几步要做
虽然这个时候已经能正常调用Python3了
```python3```
即可打开Python3的编译器。

【image】
但是系统默认调用的时候还是会指向Python2，调用起来很不爽。
人懒，直接在Sublime里面编辑了一个Bulit一个Python3，
写法是这样的：
```
{
    "cmd": ["/usr/local/bin/python3", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python"
}
```

把```"/usr/local/bin/python3"```修改成Python3的地址就可以了（记得要在默认路径保存：指定的名称.sublime-build，我的就是Python3.sublime-bulid）
【images】
至于Python3的地址可以在 terminal 当中输入```which python3```来获得,地址参考如下

> /usr/local/bin/python3

更有需要第三方套件库，安装了Anaconda的，在这个情况下无论运行Python2还是Python3显示的版本都是Default，conda命令也肯定无效，这个时候就需要在 terminal 中输入```export PATH=~/anaconda3/bin:$PATH```来将Python版本制定到Anaconda(我是这么理解 O-O)
【images】

至此，Python3的配置基本完成，可以进行任意版本的Python学习和开发了。

https://stringpiggy.hpd.io/mac-osx-python3-dual-install/#step2
https://stackoverflow.com/questions/18675907/how-to-run-conda
