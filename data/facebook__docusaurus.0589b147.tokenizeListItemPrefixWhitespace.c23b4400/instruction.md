# Bug Report

### Describe the bug

I'm experiencing an issue with markdown list parsing where list items with specific whitespace patterns are being incorrectly parsed. The problem appears to be related to how the parser handles whitespace after list item prefixes.

### Reproduction

```markdown
- Item with normal spacing
-  Item with extra space after dash
  - Nested item
```

When parsing lists with varying whitespace patterns after the list marker (dash, asterisk, etc.), the parser seems to incorrectly determine whether the whitespace is part of the list item prefix or not. This causes some valid list items to be rejected or parsed incorrectly.

### Expected behavior

The parser should correctly handle list items regardless of the amount of whitespace following the list marker, as long as it's valid markdown. All list items in the example above should be parsed as proper list items.

### Additional context

This seems to affect nested lists and lists with non-standard (but valid) spacing patterns. The issue manifests when the parser tries to determine the boundary between the list item prefix and the actual content.

---
Repository: /testbed
