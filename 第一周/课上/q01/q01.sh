#!/bin/bash
set -euo pipefail

STUDENT_ID="25060012033"

mkdir -p q01
cd q01

# 创建文件夹
mkdir -p input/docs input/tmp

# 创建各个文件
echo -e "alpha\nbeta" > "input/docs/notes one.txt"
echo "hidden" > input/docs/.secret.txt
touch input/tmp/empty.txt
echo -e "log line 1\nlog line 2" > input/run.log

# 打印绝对路径，列出input内容
pwd
ls -lA input

# 复制文件，保留目录结构，find方案（兼容空格文件名）
mkdir -p work/${STUDENT_ID}
find input -type f -name "*.txt" -exec cp --parents {} work/${STUDENT_ID}/ \;

# 修改权限
cd work/${STUDENT_ID}
find . -type d -exec chmod 750 {} \;
find . -type f -exec chmod 640 {} \;

# 生成inventory.txt，相对路径+字节数
find . -type f -printf "%P %s\n" > ../../inventory.txt
cd ../../

echo "任务完成！"
