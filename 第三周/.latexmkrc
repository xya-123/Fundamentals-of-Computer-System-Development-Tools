# 实验报告统一使用 XeLaTeX，保证 ctex 中文正常编译。
$pdflatex = 'xelatex -synctex=1 -interaction=nonstopmode -halt-on-error %O %S';
