


# Reboot第十二期实战班作业

# git提交千万不要用-f参数，遇到报错可以问、
# git提交千万不要用-f参数，遇到报错可以问、
# git提交千万不要用-f参数，遇到报错可以问、
# git提交千万不要用-f参数，遇到报错可以问、

## 不要删除别人的代码！



## 目录结果

* 01：第一次作业提交的目录
    - woniu 用自己的名字新建文件间
        + zuoye.py 作业的代码文件
    - kk kk的目录
        + zuoye.py 作业代码文件


## 1.桌面软件添加代码（推荐初学者）


[详细说明](https://github.com/shengxinjing/my_blog/issues/4)



## 2.命令行添加代码

```
第一次使用
git init
mkdir woniu
echo  print 123 >> woniu/zuoye.py
git add .
git commit -m "first commit"
git remote add origin https://github.com/51reboot/actual-12-homework.git
git push -u origin master

后面添加代码，只需要下面三行即可
git add .
git commit -m "first commit"
git push -u origin master
```

> 用命令行操作，要添加ssh的公钥到github里，操作方法


```

创建SSH key的方法很简单，执行如下命令就可以：
ssh-keygen
生成的SSH key文件保存在中～/.ssh/id_rsa.pub

然后用文本编辑工具打开该文件，我用的是vim,所以命令是：
vim ~/.ssh/id_rsa.pub

接着拷贝.ssh/id_rsa.pub文件内的所以内容，将它粘帖到github帐号管理中的添加SSH key界面中。
打开github帐号管理中的添加SSH key界面的步骤如下：
1. 登录github
2. 点击右上方的Accounting settings图标
3. 选择 SSH key
4. 点击 Add SSH key
在出现的界面中填写SSH key的名称，填一个你自己喜欢的名称即可，然后将上面拷贝的~/.ssh/id_rsa.pub文件内容粘帖到key一栏，在点击“add key”按钮就可以了。
添加过程github会提示你输入一次你的github密码

添加完成后再次执行git clone就可以成功克隆github上的代码库了。
```




账号没有加到reboot群组里的 请随时联系我
