.PHONY: all vsix install

all: vsix install

vsix:
	cd vscode && vsce package

install:
	code --install-extension vscode/*.vsix
	positron --install-extension vscode/*vsix
