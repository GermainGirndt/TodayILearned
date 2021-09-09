# Visual Studio Code - Code custom shortcuts
```
// Place your key bindings in this file to override the defaults
[
  {
    "key": "ctrl+n",
    "command": "explorer.newFile",
    "when": "explorerViewletVisible && filesExplorerFocus && !explorerResourceReadonly && !inputFocus"
  },

  {
    "key": "ctrl+shift+n",
    "command": "explorer.newFolder",
    "when": "explorerViewletVisible && filesExplorerFocus && !explorerResourceReadonly && !inputFocus"
  },
  {
    "key": "ctrl+shift+6",
    "command": "editor.action.commentLine",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+alt+z",
    "command": "merge-conflict.previous",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+alt+x",
    "command": "merge-conflict.next",
    "when": "editorTextFocus && !editorReadonly"
  }
]

```
