# 1.Shell
## date
```bash
date
```
## echo
```bash
echo "hello world"
```

- \转义  
- Don't treat the next character as special
- \也可连接多个参数
```bash
echo hello\ world

#Output: hello world

echo hello\world

#Output: helloworld

#echo 'jon's world' can't note be excecuted as there's a tailing single qupte here that doesn't get terminated
echo "jon's world"
#this command can be executed
```
## man
```bash
man <command>
# output manual of the command
```
## cd
```bash
cd <directory>
# change directory
# use relative or absolute path,  relative to the current directory
# absolute path starts with /
# . current directory
# .. parent directory of the current directory
# ~ home directory
# / root directory
# Tab 可以提示待补全的命令
```
- How does the shell even know when I type date which program to run? Like where is the date command?
- It will take the name of program and will look it up in "PATH"
- PATH is an environment variable
```bash
echo $PATH
# PATH is an environment variable in which there are a series of directories separated by :
# 当你在终端输入一个命令时，shell 会按顺序去这些目录里挨个找，找到第一个匹配的就执行
# 只存放了部分命令
```
## which
```bash
which <command> find the path of it
# It will walk through the path list and print out the place it first finds the given program
# when we run date, it will go to the directory /usr/bin/date and print out the result to the terminal
# It is more convenient to run it as we needn't get into the folder to run it 
```
```bash
which -a sh
# Output: /usr/bin/sh
#         /bin/sh
# and it will run program in the  first direcotry 
# -a输出全部信息 all
```

## ls
```bash
ls <directory>
# cat print out the content of a directory
```
## cat
```bash
cat <file>
# print out the content of the file
```
## sor & uniq
```bash
sort <file>
# 将文件中每一行排序后输出 by default字典序
uniq <file>
# 去除重复行 输出
uniq -c <file>
# 输出重复次数

sort -u <file>
# 去除重复行并排序输出
```

## head & tail
```bash
head -n3 <file>
# 输出<file>的前三行

tail -n3 <file>
# 输出<file>的后三行
```
## grep
```bash
grep  
# a file searcher
# It searches for things that match a particular pattern
# accept two argument pattern & a list of files
grep 3 data
# It will print out all the lines that match the pattern that you gave in
# Output: 3 31 3
# We can use grep and regular expression to search some difficult things like the first character is not A and the second character is a number

grep -r "pattern" .
grep -r grep .
# -r for recursive, go deeply into all the nested folders from the current folder, search all of those files for grep 找所有当前目录下所有文件中的grep

```

## sed
```bash
sed
# a line editor that is intended to be programed 可编程行编辑器
sed -i 's/grep/jon/g' <file>
# 将所有文件替换成jon
# -i 对原文件进行操作
# s means substitute
# g means global
#  
sed -i.bak 's/grep/jon/g' file.txt
#生成 file.txt.bak 原文件备份
#修改file.txt

sed -i 's/grep/jon/g' */*.md
# 任何目录中所有以.md结尾的文件都执行这个操作

# glob 通配符模式
# *  任意多个字符
# ?  任意一个字符
```
## git ...
```bash
git diff
# 目录需要含有.git文件
# 输出原内容与更改后的内容
```
## find
```bash
find ~/Downloads -type f -name "*.zip" -mtime +30
# 可使用丰富的参数列表使其可以找到各种各样的文件
# 查找Downloads目录下的file 名字以.zip结尾 且在三十天内没有被修改过
find ~/Downloads -type f -size +100M -exec ls -lh {} \；
# -exec在此意为 符合 type为file size>100M的文件，执行以下程序
# -l意为more information 显示读写执行权限
# -h意为以人类可读的格式显示文件大小
# -a可显示被隐藏的程序
# {} 被替换为找到的路径 占位符
#  \;表明程序结束  后面可加-mtime之类的参数用于筛选文件

find . -name "*.md" -exec grep -l "TODO" {} \;
# 找到所有含有"TODO" 的.md文件并且打印出文件名
# grep中的-l 表示files with matches 只显示文件名 改变了输出内容

# find 默认递归 但可以设置最大搜索深度 -maxdepth 0只看当前目录 -maxdepth 1 只看当前目录和下一目录

find . -type d -name "*project*"
#找出当前目录下包含"project"的所有子目录
```

## awk
```text
#data
a b c
d e f
g h i
```

```bash
awk 
# 按照空白字符和行来分隔并执行命令？
awk '{print $2}' data
# 花括号内代表要执行的程序
# 输出每一行的第二个字符
#Output:
#b
#e
#h

awk -F, '{print $2}' data
# -F filed separater 以,为分隔符分隔
```

## | & > & <
| 符号 | 名称 | 作用 |
| :---: | :--- | :--- |
| `\|` | 管道符 | 把左边命令的输出，传给右边的**命令**处理 |
| `>` | 输出重定向 | 把左边命令的输出，写入右边的**文件** |
| `>>` | 追加重定向 | 同上，但保留原内容，追加到末尾 |
| `<` | 输入重定向 | 把右边**文件**的内容，作为左边命令的输入 |
## ?
```bash
if grep 2026 thedate.text; then echo "It's 2026"; echo "Hello";fi

# exit successfully with 0 unsuccessfully with nonezero

while grep 2026 thedate.txt; do echo "it's still 2026"; data > thedate.txt;done

for varname in a b c d; do echo "$varname"; done

# 变为熟悉的for 循环
for varname in $(seq 1 10)
for varname in $(seq 1 10 2)

if ["hello"="world"]; then echo "equal";else echo "not equal" fi

if [-f thedata.txt]; then echo "thedate exists"; fi
# -f used to examine whether the file exist
```

## .sh
- 命令太长可写成.sh脚本
```bash
#!/usr/bin/sh
# tells the shell when someone runs this file, find the program in this path then put the file as the input of the program

# execute
/usr/bin/sh < <file>
# 通过“我”(主体)去执行该文件 该文件不需要有x执行权限。
# 内核执行.sh文件 sh读a.sh 只需要r权限

# ./会失效，因为没有权限执行
# ./只是在当前目录下找该文件，当该文件有x (被标记为可执行文件)，则会运行

# x权限是内核允许把这个文件当程序加载的许可，x本身并不赋予文件被执行的能力，只是发放许可。 没有x，内核不认为其是可执行文件
```
## chmod
```bash
# -rwxr-xr-x
# 拥有者user 所属组group 其他人others
# rwx read write execute三种权限
chmod +x a.sh          # 所有人加执行
chmod u+x a.sh         # 只给所有者加执行
chmod go-w a.sh        # 组和其他人去掉写
chmod u=rwx a.sh       # 所有者设为 rwx
chmod a+r a.sh         # 所有人加读

chmod 755 a.sh    # rwxr-xr-x
chmod 644 a.sh    # rw-r--r--
chmod 700 a.sh    # rwx------
# 111对应十进制的7

# 常用参数
#-R 递归作用于目录下所有文件
chmod -R 755 mydir/
# -v 显示详细过程
```



# 2.命令行环境


