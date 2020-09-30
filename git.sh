FILE = $PWD
for f in $FILES
do
    git add git.sh
    git commit -m"${message}"
    if [ -n "$(git status - porcelain)" ];
    then
        echo "IT IS CLEAN"
    else
        git status
        echo "Pushing data to remote server!!!"
        git push origin master
    fi
done
