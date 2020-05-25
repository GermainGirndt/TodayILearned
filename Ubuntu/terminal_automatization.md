# Terminal Automatization


## Move multiple files in current folder


#### Test first

```
for f in *django*; do echo git mv -v -- "$f" django ; done
```

#### Do
```
for f in *django*; do git mv -v -- "$f" django ; done
```