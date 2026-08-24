#!/bin/bash
set -euo pipefail

#接收第一个参数：csv文件路径
CSV="$1"

# 判断文件是否存在；不存在输出错误到stderr，退出码非0
if [[ ! -f "${CSV}" ]]; then
    echo "error: 文件 ${CSV} 不存在" >&2
    exit 1
fi

echo "==== 5xx最多的前2个path（次数降序，次数相同按path字典序） ===="

# -F, 逗号分隔；NR>1跳过表头；status($4)以5开头；统计path；排序取前2
awk -F',' 'NR>1 && $4 ~ /^5/ {print $3}' "${CSV}" \
| sort \
| uniq -c \
| sort -k1,1nr -k2,2 \
| head -n 2

echo -e "\n==== 全部数据行平均latency_ms（保留两位小数） ===="

# NR>1跳过表头，累加latency总和、计数；用awk做浮点计算保留2位
awk -F',' 'NR>1 {sum += $5; cnt+=1} END {printf "%.2f\n", sum/cnt}' "${CSV}"
