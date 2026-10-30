#!/usr/bin/env python3
"""
Theme validation: duplicate scopes across rules, redundant scopes within a rule
"""

import json
import sys
from collections import defaultdict


def covers(prefix, scope):
    return scope == prefix or scope.startswith(prefix + ".")


def scopes_of(rule):
    scopes = rule.get("scope", [])
    return [scopes] if isinstance(scopes, str) else scopes


def find_duplicates(rules):
    seen = defaultdict(list)
    for i, rule in enumerate(rules):
        for scope in scopes_of(rule):
            seen[scope].append(rule.get("name", f"Rule {i}"))
    return {s: names for s, names in seen.items() if len(names) > 1}


def find_redundant(rules):
    """Scopes already covered by a broader scope in the same rule.

    Only flagged when no other rule sits in between, since then removing the
    narrower scope could change which rule wins.
    """
    others = [(i, s) for i, r in enumerate(rules) for s in scopes_of(r) if " " not in s]
    redundant = []
    for i, rule in enumerate(rules):
        plain = [s for s in scopes_of(rule) if " " not in s]
        for s in plain:
            for p in plain:
                if p == s or not covers(p, s):
                    continue
                between = any(j != i and q != p and covers(p, q) and covers(q, s) for j, q in others)
                if not between:
                    redundant.append((rule.get("name"), s, p))
                    break
    return redundant


def main(path):
    with open(path) as f:
        rules = json.load(f).get("tokenColors", [])

    ok = True
    for scope, names in find_duplicates(rules).items():
        print(f"duplicate scope {scope!r} in rules: {', '.join(names)}")
        ok = False
    for name, scope, broader in find_redundant(rules):
        print(f"redundant scope {scope!r} in rule {name!r}, covered by {broader!r}")
        ok = False

    if ok:
        print(f"✓ {len(rules)} token rules, no duplicate or redundant scopes")
    return ok


if __name__ == "__main__":
    sys.exit(0 if main("vscode/themes/monokai-spacegray-eighties.json") else 1)
