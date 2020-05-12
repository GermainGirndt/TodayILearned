
# Enviroment Settings for Sublime Text

Based on Corey Schafer's videos

### Install following Packages:

1. Sublime Code Intel (code completion)
2. SublimeLinter (and not SublimeLint!) + individual packages
3. Anaconda

#### Personal Settings - Anaconda

```
{
    "auto_formatting": true,

    "autoformat_ignore":
    [
        "E309",
        "E501"
    ],


    "pep8_ignore":
    [
        "E309",
        "E501"
    ]
}
```


**If python interpreter not found:**   

```
cd usr/bin    
sudo cp -n -R python3 python    
```

#### Building a new enviroment with Sublime


```
{
    "cmd": ["/usr/bin/python3", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "quiet": false,
    "selector": "source.python"
}
```