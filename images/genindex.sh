#！/usr/bin/bash

files=$(ls)
main=index.html
cat /dev/null > $main
echo '<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>Resources</title></head><body><ul>' > $main
for i in $files; do
  if [ $i != 'index.html' ] && [ $i != 'genindex.sh' ]; then
    echo '<li><a href="'$i'">'$i'</a></li>' >> $main
  fi
done
echo '</ul></body></html>' >> $main
echo '首页文件生成完毕'
