
echo "hello word"

mkdir "new_dir"

cd new_dir
rm -r new_dir

cp -r lorem lorem-copy
cp lorem/sed.txt lorem-copy/sed-copy.txt

head lorem/sed.txt

head lorem/at.txt

head -n 3 lorem-copy/sed.txt

echo "Homo homini lupus." lorem-copy/sed.txt

tail -n 3 lorem-copy/sed.txt

whoami

pwd

ls lorem/*.txt

ls -als lorem/sed.txt

find . -type f -name "lorem*" | wc -l

grep -o 'et' lorem/at.txt | wc -l

## Ficheros bash

```

touch list_files.sh

#### abrir el archivo en visual studio code
echo 'ls' >> list-files.sh 
chmod +x list-files.sh #### cambiar permisos
./list-files.sh #### ejecutar
bash list_files.sh #### otra opcion para ejecutar
