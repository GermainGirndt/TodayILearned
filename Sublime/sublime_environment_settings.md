
# Enviroment Settings for Sublime Text

Based on Corey Schafer's videos

### Install following Packages:

1. Sublime Code Intel (code completion)
2. SublimeLinter (and not SublimeLint!) + individual packages
3. Anaconda
4. Terminus - Integrated Terminal Window (https://packagecontrol.io/packages/Terminus)
5. Djaneiro (django) - https://packagecontrol.io/packages/Djaneiro

##### HTML-Linter Package



Terminal:
```
sudo apt install tidy
```

Sublime:
```
SublimeLinter-html-tidy
```

##### Personal Settings - Anaconda Package

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


#### Terminus - Personal theme settings

```
{
    "theme": "default",
    "user_theme_colors":
    {
        "00": "#000000",
        "background": "#000000",
        "block_caret": "light_white",
        "caret": "light_white",
        "selection": "#000000"
    },
    "view_settings":
    {
        "font_size": 10
    }
}

```