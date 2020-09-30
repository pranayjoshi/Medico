for f in $PWD;
do
    git add $f
    git commit -m "initial commit"
    git push origin master
done
