.PHONY: all vsix install

EXTPATH=vscode
NAME=$(shell jq -r ".name" < $(EXTPATH)/package.json)
VERSION=$(shell jq -r ".version" < $(EXTPATH)/package.json)


VSIX=$(EXTPATH)/$(NAME)-$(VERSION).vsix

all: install

$(VSIX): clean
	cd $(EXTPATH) && vsce package


install: $(VSIX)
	code --install-extension $(VSIX)
	positron --install-extension $(VSIX)

clean:
	-rm $(EXTPATH)/*vsix
