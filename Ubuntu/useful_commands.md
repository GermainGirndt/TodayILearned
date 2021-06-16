## Useful Commands


#### Machine

* **Machine Name**
```
uname -a
```

* **Get Machine Information (Model, Serial, etc...)**
```
sudo dmidecode | grep -A 10 "System Information"
```


#### SecureBoot
```
sudo mokutil --enable-validation

sudo mokutil --disable-validation
```

#### Extracting g tar - verbose
```
tar xvzf FILENAME.tar.gz 
```

#### Installing .sh file

* **Give write permission**
```
chmod +x /path/to/yourscript.sh
```

* **Run file with './'**
```
./yourscript.sh
```
and **NOT**

```
yourscript.sh
```

* **get ip from dns*
```
nslookup google.com
```
