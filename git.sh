for f in *;
do
    git add $f
    git commit -m "initial commit"
    git push origin master
done
