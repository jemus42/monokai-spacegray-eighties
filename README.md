# Monokai Spacegray Eighties

An editor theme I kind of got used to a lot.

I got it off of a TextMate theme editor webapp thingy a while back, imported it to RStudio 
(which understood the `.tmTheme` format and converted it to its CSS format (I think)), 
and now I would like to use it with [Positron](https://positron.posit.co/) so I had to try 
to convert to to the VSCode format.

Disclaimer: I used Claude for the conversion from tmTheme to VScode and threw in the 
rstheme for good measure and honestly I haven't done any kind of fine-tuning yet YMMV.

Still in need of fixing:

- JSON
- CSS
- Okay basically everything that isn't R specifically isn't looking _great_.


## Building for VSCode / Positron

```sh
cd vscode
vsce package

# Install for VSCode
code --install-extension *vsix

# Install for Positron
positron --install-extension *vsix
```


## Credit

Original (I think?) TextMate theme from [pyoio](https://github.com/pyoio/monokai-spacegray)
