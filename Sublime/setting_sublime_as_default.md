# Setting Sublime as Default Text Editor

(Reference: https://askubuntu.com/questions/396938/how-do-i-make-sublime-text-3-the-default-text-editor)

### If `/usr/share/applications/sublime_text.desktop` exists:

**Open on your Terminal:**

    subl /usr/share/applications/defaults.list

Search for all instances of the standard `gedit` (probably with a longer name) and replace them with `sublime_text`.


---
### Else:

**Create `sublime-text.desktop`:**

    sudo touch /usr/share/applications/sublime_text.desktop

**Open it in Sublime:**

    subl /usr/share/applications/sublime_text.desktop

**and paste the following into it:**

    [Desktop Entry]
    Version=1.0
    Type=Application
    Name=Sublime Text
    GenericName=Text Editor
    Comment=Sophisticated text editor for code, markup and prose
    Exec=/opt/sublime_text/sublime_text %F
    Terminal=false
    MimeType=text/plain;
    Icon=sublime-text
    Categories=TextEditor;Development;
    StartupNotify=true
    Actions=Window;Document;
    
    [Desktop Action Window]
    Name=New Window
    Exec=/opt/sublime_text/sublime_text -n
    OnlyShowIn=Unity;
    
    [Desktop Action Document]
    Name=New File
    Exec=/opt/sublime_text/sublime_text --command new_file
    OnlyShowIn=Unity;
