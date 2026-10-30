# Monokai Spacegray Eighties theme tasks
# Requires: jq, npx (Node), uv; code and/or positron for installing

extpath := "vscode"
name := `jq -r ".name" < vscode/package.json`
publisher := `jq -r ".publisher" < vscode/package.json`
version := `jq -r ".version" < vscode/package.json`
vsix := name + "-" + version + ".vsix"
vsce := "npx --yes @vscode/vsce@4"

default: install

# Remove built packages
clean:
    -rm -f {{extpath}}/*.vsix

# Check theme scopes and JSON validity
validate:
    jq empty {{extpath}}/package.json {{extpath}}/themes/*.json
    uv run validate_theme.py

# Build the .vsix package
build: clean validate
    cd {{extpath}} && {{vsce}} package

# Install into VS Code and Positron
install: install-vsc install-positron

# Install into VS Code
install-vsc: build
    @if command -v code >/dev/null 2>&1; then code --install-extension {{extpath}}/{{vsix}}; else echo "VS Code not found, skipping"; fi

# Install into Positron
install-positron: build
    @if command -v positron >/dev/null 2>&1; then positron --install-extension {{extpath}}/{{vsix}}; else echo "Positron not found, skipping"; fi

# Uninstall from VS Code and Positron
uninstall:
    -code --uninstall-extension {{publisher}}.{{name}}
    -positron --uninstall-extension {{publisher}}.{{name}}

# Regenerate the icons
icon:
    uv run create_icon.py

# Publish to Open VSX manually (needs OVSX_PAT); normally done by pushing a v* tag
publish: build
    cd {{extpath}} && npx --yes ovsx@1 publish {{vsix}}
