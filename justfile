# Monokai Spacegray Eighties Theme Build Scripts
# Requires: jq, vsce, code, positron

# Default recipe (equivalent to 'make all')
default: install

# Variables
extpath := "vscode"
name := `jq -r ".name" < vscode/package.json`
version := `jq -r ".version" < vscode/package.json`
vsix := extpath / name + "-" + version + ".vsix"

# List all available recipes
list:
    @echo "Available recipes:"
    @just --list --unsorted

# Clean build artifacts
clean:
    @echo "Cleaning build artifacts..."
    -rm {{extpath}}/*.vsix

# Build the VSIX package
build: clean
    @echo "Building VSIX package..."
    cd {{extpath}} && vsce package
    @echo "Built: {{vsix}}"

# Install extension to editors
install: build
    @echo "Installing extension to VS Code and Positron..."
    @if command -v code >/dev/null 2>&1; then \
        echo "Installing to VS Code..."; \
        code --install-extension {{vsix}}; \
    else \
        echo "VS Code not found, skipping..."; \
    fi
    @if command -v positron >/dev/null 2>&1; then \
        echo "Installing to Positron..."; \
        positron --install-extension {{vsix}}; \
    else \
        echo "Positron not found, skipping..."; \
    fi
    @echo "Installation complete!"

# Package without installing
package: build
    @echo "Package created: {{vsix}}"

# Show package information
info:
    @echo "Package: {{name}}"
    @echo "Version: {{version}}"
    @echo "VSIX: {{vsix}}"
    @echo "Extension path: {{extpath}}"

# Validate package.json and theme
validate:
    @echo "Validating package.json..."
    @jq empty {{extpath}}/package.json && echo "✓ package.json is valid JSON"
    @echo "Validating theme..."
    @uv run python validate_theme.py

# Lint the theme files
lint: validate
    @echo "Linting theme files..."
    @if [ -f "{{extpath}}/themes/monokai-spacegray-eighties.json" ]; then \
        jq empty {{extpath}}/themes/monokai-spacegray-eighties.json && echo "✓ Theme file is valid JSON"; \
    else \
        echo "✗ Theme file not found"; \
        exit 1; \
    fi

# Check prerequisites
check:
    @echo "Checking prerequisites..."
    @command -v jq >/dev/null 2>&1 || (echo "✗ jq not found" && exit 1)
    @command -v vsce >/dev/null 2>&1 || (echo "✗ vsce not found (run: npm install -g vsce)" && exit 1)
    @echo "✓ Prerequisites check passed"

# Full build and test pipeline
ci: check lint package
    @echo "CI pipeline completed successfully!"

# Watch for changes and rebuild (requires entr or similar)
watch:
    @echo "Watching for changes... (requires 'entr' to be installed)"
    @if command -v entr >/dev/null 2>&1; then \
        find {{extpath}} -name "*.json" | entr -r just build; \
    else \
        echo "Install 'entr' for file watching: brew install entr"; \
        exit 1; \
    fi

# Uninstall extensions from editors
uninstall:
    @echo "Uninstalling extension from editors..."
    @if command -v code >/dev/null 2>&1; then \
        echo "Uninstalling from VS Code..."; \
        code --uninstall-extension {{name}} || true; \
    fi
    @if command -v positron >/dev/null 2>&1; then \
        echo "Uninstalling from Positron..."; \
        positron --uninstall-extension {{name}} || true; \
    fi
    @echo "Uninstall complete!"

# Publish to marketplace (be careful!)
publish: ci
    @echo "Publishing to VS Code marketplace..."
    @read -p "Are you sure you want to publish? [y/N]: " confirm && [ "$$confirm" = "y" ]
    cd {{extpath}} && vsce publish