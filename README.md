# Monokai Spacegray Eighties

[![Open VSX version](https://img.shields.io/open-vsx/v/jemus42/monokai-spacegray-eighties)](https://open-vsx.org/extension/jemus42/monokai-spacegray-eighties)

A dark Monokai theme on a neutral gray background, made for R and Quarto in [Positron](https://positron.posit.co/).

It started as a TextMate theme I picked up years ago (original by [pyoio](https://github.com/pyoio/monokai-spacegray)) and used in RStudio, and this is the port to Positron and VS Code.
The original `.tmTheme` and RStudio `.rstheme` are kept in this repository for reference.

## Palette

| Color | Used for |
|---|---|
| `#F92672` pink | keywords, operators, tags |
| `#66D9EF` cyan | function calls, builtin types, links, UI accents |
| `#A6E22E` green | function and class definitions, headings, package namespaces |
| `#E6DB74` yellow | strings |
| `#AE81FF` purple | numbers and constants |
| `#FD971F` orange | parameters, inline code in Markdown |
| `#808080` gray | comments |

The terminal and the Positron console get a matching ANSI palette, so cli and testthat output fits in.

## Installation

Install it from [Open VSX](https://open-vsx.org/extension/jemus42/monokai-spacegray-eighties), which is where Positron gets its extensions, or search the Extensions view for "Monokai Spacegray Eighties".
Then pick it with **Preferences: Color Theme**.

## Notes

Positron is the primary target.
Its R grammar differs from the one in VS Code and the REditorSupport extension, so R code may look slightly different in VS Code.

## Development

Build and install locally with [just](https://github.com/casey/just), which needs `jq`, Node (for `npx`) and [uv](https://docs.astral.sh/uv/):

```sh
just install           # validate, build the .vsix, install into VS Code and Positron
just install-positron  # Positron only
just validate          # check the theme for duplicate or redundant scopes
just uninstall
```

`demo/` has R, Python and Quarto files for checking the highlighting.
**Developer: Inspect Editor Tokens and Scopes** shows which scopes and theme rule apply to a token.

To release, rename the `[Unreleased]` section in `CHANGELOG.md` to the version from `vscode/package.json`, commit, and push a matching `v*` tag.
The release workflow then publishes to Open VSX (using the `OVSX_TOKEN` repository secret) and creates a GitHub release with that changelog section as notes.
