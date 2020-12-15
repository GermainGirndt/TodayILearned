# Terminal Automation

## Rename ONLY file content in directories recursively

```
find . -type f -exec sed -i 's/contentToBeReplaced/newContent/g' {} \;
``` 

## Rename ONLY file AND directory names recursively

```
find directoryToRenameRecursively/ -exec rename 's/team/workflow/g' '{}' \;
```



## Move multiple files in current folder


#### Test first

```
for f in *django*; do echo git mv -v -- "$f" django ; done
```

#### Do
```
for f in *django*; do git mv -v -- "$f" django ; done
```

## Kill Process On Port

#### Write it into `~./bashrc`
```
alias killport='
kill_process () {     sudo kill -9 $(sudo lsof -t -i:$1); }
kill_process '
```
