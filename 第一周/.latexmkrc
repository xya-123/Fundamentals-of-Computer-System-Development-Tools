# 实验报告统一走 XeLaTeX（ctex 中文支持）
# 注意：命令行参数 latexmk -pdf 会覆盖 rc 里的 $pdf_mode，
# 所以这里直接把 $pdflatex 替换成 xelatex，使
#   latexmk -pdf -halt-on-error 实验报告.tex
# 实际用 XeLaTeX 编译，中文正常。
$pdflatex = 'xelatex -synctex=1 -interaction=nonstopmode -halt-on-error %O %S';
