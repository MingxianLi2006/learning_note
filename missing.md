# 1.Shell
```bash
date

echo "hello world"

\转义

echo 'jon's world'
无法实现

man <command>
//output manual of the command

cd change directory
use relative or absolute path
. current directory
.. parent directory of the current directory
~ home directory
/ root directory
Tab 可以提示待补全的命令

which <command> find the path of it

-a输出全部信息

ls list

cat print out the content of a file

sort <file>
排序后输出

uniq <file>
去除重复项 排序输出

grep  a file searcher

head

tail

sed

glob

'g全局替换？

通配符 *




find  
used to find the file
find ~/Downloads -type f -name "*.zip" -mtime+30

find ~/Downloads -type f -size +100M -exec ls -lh


ctrl C 

find . -name "*.md" -exec grep -l "TODO" {} \;

awk 
used to parse file
parsing?

a b c
d e f
g h i
awk '{print $2}' data

ssh



tail -n 10

|
run the left program take the output and use it as the input of the right program


>

<






```

# 2.命令行环境


