# Joining zip files

```
cat test.zip.* > test.zip
zip -FF test.zip --out test-full.zip # fixes the cat
unzip test-full.zip
```

## For large files, **use Java**

- **Install**

```
sudo apt install -y default-jdk              # version 2:1.11-72, or
sudo apt install -y openjdk-11-jdk-headless  # version 11.0.11+9-0ubuntu2~20.04
sudo apt install -y openjdk-16-jdk-headless  # version 16.0.1+9-1~20.04
sudo apt install -y openjdk-8-jdk-headless   # version 8u292-b10-0ubuntu1~20.04
sudo apt install -y fastjar                  # version 2:0.98-6build1
sudo apt install -y openjdk-13-jdk-headless  # version 13.0.7+5-0ubuntu1~20.04
```

- **Use**

```
jar xvf file.zip
```
