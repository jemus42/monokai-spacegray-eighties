#!/usr/bin/env python3
"""
Theme validation script to check for duplicates and conflicts
"""

import json
from collections import defaultdict, Counter

def validate_theme(theme_path):
    with open(theme_path, 'r') as f:
        theme = json.load(f)
    
    print("🎨 Theme Validation Report")
    print("=" * 50)
    
    token_colors = theme.get('tokenColors', [])
    print(f"📊 Total rules: {len(token_colors)}")
    
    # Track scope usage
    scope_to_rules = defaultdict(list)
    scope_colors = defaultdict(set)
    
    for i, rule in enumerate(token_colors):
        rule_name = rule.get('name', f'Rule {i}')
        scopes = rule.get('scope', [])
        color = rule.get('settings', {}).get('foreground')
        
        if isinstance(scopes, str):
            scopes = [scopes]
        
        for scope in scopes:
            scope_to_rules[scope].append((i, rule_name))
            if color:
                scope_colors[scope].add(color)
    
    # Find duplicates
    duplicates = {scope: rules for scope, rules in scope_to_rules.items() if len(rules) > 1}
    
    if duplicates:
        print("\n⚠️  DUPLICATE SCOPES:")
        for scope, rules in duplicates.items():
            colors = list(scope_colors[scope])
            print(f"  • {scope}")
            for rule_idx, rule_name in rules:
                rule_color = token_colors[rule_idx].get('settings', {}).get('foreground', 'none')
                print(f"    - Rule #{rule_idx}: {rule_name} → {rule_color}")
            if len(colors) > 1:
                print(f"    ⚠️  CONFLICT: Multiple colors {colors}")
            print()
    else:
        print("\n✅ No duplicate scopes found!")
    
    # Check for unused base scopes
    print("\n📋 SCOPE COVERAGE:")
    base_scopes = ['source.r', 'text.html.quarto', 'variable', 'keyword', 'string', 'comment', 'constant']
    for base in base_scopes:
        matching = [s for s in scope_to_rules.keys() if base in s]
        print(f"  • {base}: {len(matching)} rules")
    
    # Color usage
    print("\n🎨 COLOR USAGE:")
    all_colors = [rule.get('settings', {}).get('foreground') for rule in token_colors]
    color_counts = Counter(c for c in all_colors if c)
    for color, count in color_counts.most_common():
        print(f"  • {color}: {count} rules")
    
    return len(duplicates) == 0

if __name__ == "__main__":
    is_valid = validate_theme("vscode/themes/monokai-spacegray-eighties.json")
    exit(0 if is_valid else 1)