#!/usr/bin/env python3
"""
Clean up theme duplicates and conflicts
"""

import json
from collections import defaultdict

def clean_theme():
    with open("vscode/themes/monokai-spacegray-eighties.json", 'r') as f:
        theme = json.load(f)
    
    # Start with essential base rules
    cleaned_rules = [
        {
            "name": "Comments",
            "scope": [
                "comment",
                "comment.line",
                "comment.block",
                "comment.documentation",
                "punctuation.definition.comment",
                "source.r comment.line.number-sign.r",
                "text.html.quarto comment"
            ],
            "settings": {
                "fontStyle": "italic",
                "foreground": "#808080"
            }
        },
        {
            "name": "Strings",
            "scope": [
                "string",
                "string.quoted",
                "string.template",
                "string.interpolated",
                "string.regexp"
            ],
            "settings": {
                "foreground": "#E6DB74"
            }
        },
        {
            "name": "Numbers and Constants",
            "scope": [
                "constant.numeric",
                "constant.language",
                "constant.character",
                "constant.other",
                "constant.language.boolean",
                "constant.language.null",
                "constant.language.undefined",
                "constant.language.nil"
            ],
            "settings": {
                "foreground": "#AE81FF"
            }
        },
        {
            "name": "String Escapes",
            "scope": [
                "constant.character.escape",
                "constant.other.placeholder"
            ],
            "settings": {
                "foreground": "#AE81FF"
            }
        },
        {
            "name": "Keywords",
            "scope": [
                "keyword",
                "keyword.control",
                "keyword.other",
                "storage",
                "storage.modifier"
            ],
            "settings": {
                "foreground": "#F92672"
            }
        },
        {
            "name": "Operators",
            "scope": [
                "keyword.operator",
                "keyword.operator.assignment",
                "keyword.operator.arithmetic", 
                "keyword.operator.logical",
                "keyword.operator.comparison",
                "keyword.operator.pipe.r",
                "keyword.operator.infix.r",
                "keyword.operator.r",
                "punctuation.accessor",
                "punctuation.separator.comma",
                "punctuation.terminator.statement"
            ],
            "settings": {
                "foreground": "#F92672"
            }
        },
        {
            "name": "Storage Types",
            "scope": [
                "storage.type",
                "storage.type.r"
            ],
            "settings": {
                "fontStyle": "italic",
                "foreground": "#66D9EF"
            }
        },
        {
            "name": "Variables",
            "scope": [
                "variable",
                "variable.other",
                "variable.other.readwrite",
                "variable.language.this",
                "variable.language.self",
                "variable.language.super",
                "variable.other.r",
                "text.html.quarto variable.object"
            ],
            "settings": {
                "foreground": "#F8F8F8"
            }
        },
        {
            "name": "Function Parameters",
            "scope": [
                "variable.parameter",
                "variable.parameter.r",
                "meta.function.parameters variable.parameter",
                "meta.function.declaration variable.parameter",
                "meta.function.call.arguments variable.parameter"
            ],
            "settings": {
                "fontStyle": "italic",
                "foreground": "#FD971F"
            }
        },
        {
            "name": "Function Calls - All Cyan",
            "scope": [
                "entity.name.function",
                "support.function",
                "variable.function",
                "meta.function-call",
                "source.r entity.name.function.r",
                "source.r variable.function.r",
                "text.html.quarto entity.name.function",
                "text.html.quarto variable.function.r"
            ],
            "settings": {
                "foreground": "#66D9EF"
            }
        },
        {
            "name": "Function Definitions - Green Override",
            "scope": [
                "meta.function entity.name.function",
                "meta.definition.function entity.name.function",
                "source.r meta.function.r entity.name.function"
            ],
            "settings": {
                "foreground": "#A6E22E"
            }
        },
        {
            "name": "Classes and Types",
            "scope": [
                "support.class",
                "support.type",
                "entity.name.class",
                "entity.name.type",
                "entity.other.inherited-class"
            ],
            "settings": {
                "fontStyle": "italic",
                "foreground": "#66D9EF"
            }
        },
        {
            "name": "Module Names",
            "scope": [
                "entity.name.namespace",
                "entity.name.module",
                "support.other.module"
            ],
            "settings": {
                "foreground": "#A6E22E"
            }
        },
        {
            "name": "Markup Headers",
            "scope": [
                "markup.heading",
                "entity.name.section.markdown",
                "entity.name.section.quarto",
                "markup.heading.quarto",
                "heading.1.quarto",
                "heading.2.quarto", 
                "heading.3.quarto",
                "heading.4.quarto",
                "heading.5.quarto",
                "heading.6.quarto"
            ],
            "settings": {
                "fontStyle": "bold",
                "foreground": "#A6E22E"
            }
        },
        {
            "name": "Invalid/Error",
            "scope": [
                "invalid",
                "invalid.illegal"
            ],
            "settings": {
                "background": "#F92672",
                "foreground": "#F8F8F8"
            }
        }
    ]
    
    theme['tokenColors'] = cleaned_rules
    
    with open("vscode/themes/monokai-spacegray-eighties.json", 'w') as f:
        json.dump(theme, f, indent=4)
    
    print(f"✅ Cleaned theme: {len(cleaned_rules)} rules (was 70)")

if __name__ == "__main__":
    clean_theme()