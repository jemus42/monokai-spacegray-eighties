# Changelog

## [0.1.0] - 2026-10-30

### Added

- Terminal and Positron console ANSI palette in Monokai colors, with Spacegray Eighties blue.
- Markdown and Quarto inline styles: bold, italic, strikethrough, orange inline code, cyan links, gray italic quotes.
- Workbench colors for the title bar, tab strip, widgets, inputs, lists, buttons, badges, focus ring and the activity bar's active indicator, replacing the leftover vs-dark grays and blues.
- Pink error text in the Positron console.
- Restored from the original TextMate theme: tag names, tag attributes (e.g. YAML keys in Quarto front matter), library constants, deprecated markers and diff colors.

### Changed

- Selection is blue-gray (`#3E4A57`) so it stays visible on the current line and inside Quarto code chunks.
- Class names are green again, as in the original theme.
- Commas and semicolons are no longer pink.

### Fixed

- Matching brackets were highlighted in red because the color was not in hex format.
