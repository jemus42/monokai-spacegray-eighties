# Monokai Spacegray Eighties

An editor theme I kind of got used to a lot.

I got it off of a TextMate theme editor webapp thingy a while back, imported it to RStudio 
(which understood the `.tmTheme` format and converted it to its CSS format (I think)), 
and now I would like to use it with [Positron](https://positron.posit.co/) so I had to try 
to convert to to the VSCode format.

Disclaimer: I used Claude heavily for the conversion from tmTheme to VScode and threw in the 
rstheme for good measure and honestly I'm just trial-and-erroring my way towards a usable theme.

The primary target for the R syntax is Positron, so if it doesn't look exactly correct for VSCode with the REditorSupport R extension: Yes, I know, sorry about that, it is a compromise.

I also tried to make quarto documents look okay but everything about this is quite WIP.

## Building for VSCode / Positron

Either use `just install` or do it manually:

```sh
cd vscode

# Build the extensions, needs the vsce tool installed via npm.
vsce package

# Install for VSCode
code --install-extension *vsix

# Install for Positron
positron --install-extension *vsix
```


## Credit

Original (I think?) TextMate theme from [pyoio](https://github.com/pyoio/monokai-spacegray)
