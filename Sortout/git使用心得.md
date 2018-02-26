### 准备工作
设置本机Git账号和邮箱
```
git config  --global user.name "USERNAME"
git config -- global user.email "EMAIL"
```
如需使用远程仓库功能还需生成ssh key来确保能同步远程
```
ssh-keygen -t rsa -C "EMAIL"
```
创建期间需要确认，全部回车即可创建成功， key保存在id_rsa.pub当中

>mac文件路径：  /User/mac/.ssh /
win文件路径/用户/.ssh/

将文件内的所有内容复制，粘贴到远程仓库的公钥库当中既可。


### 基本使用

        git status   # 查看当前版本库状态
        git add (-A)    # 将修改的内容添加到版本记录当中， 参数-A 添加所有文件
        git commit  -m ""    # 提交已经添加的修改， 参数 -M "" 的双引号内输入增加的备注
        git push 推送远程版本库
        om  git pull 获取远程版本库

### git 远程拉取本地不存在的分支
        git branch    # 查看当前的本地的所有分支
        git checkout -b 目标分支    # 建立新的分支
        git checkout -b 本地分支名称 /origin/远程分支名称   # 将远程分支和本地分支建立连接

