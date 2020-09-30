for f in *;
do
    echo "filename = ${f}"
    git add $f
    git commit -m "initial commit"
    git push origin master
done
