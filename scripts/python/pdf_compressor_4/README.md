# Scripts used in MacOS's commandline

### Option 1 - Cups Filter

cupsfilter -m application/pdf -c input.pdf > output.pdf

### Option 2 - Cups Filter

```
Compression Levels (-dPDFSETTINGS)

/screen: Low quality, smallest file size.
/ebook: Medium quality.
/printer: High quality.
/prepress: Maximum quality.
```

- Command:

```
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dBATCH -dQUIET -sOutputFile=output-gs-ebook.pdf Einkommenserklaerung\ \ unterschrieben.pdf
```
