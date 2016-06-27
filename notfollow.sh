# Не следить за изменениями в файлах
git update-index --assume-unchanged ./functions/authData.py
echo 'Отключена git слежка за файлом ./functions/authData.py (данные ВК)'
git update-index --assume-unchanged ./script.sh
echo 'Отключена слежка за изменениями в файле ./script.py (в нем указан путь до скрипта)'
