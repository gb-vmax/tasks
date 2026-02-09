# Bug Report

### Describe the bug

I'm encountering an issue with list item parsing where whitespace handling in list item prefixes seems broken. When parsing markdown lists, items that should be properly recognized are being rejected or parsed incorrectly.

### Reproduction

```markdown
- Item 1
  - Nested item with proper indentation
    - Double nested item
```

The nested list items don't get parsed correctly - they're either being treated as continuation of the parent item or rejected entirely. This is affecting both ordered and unordered lists with nested structures.

### Expected behavior

Nested list items with correct indentation (2-4 spaces typically) should be properly recognized and parsed as child list items, not rejected or misinterpreted.

### Additional context

This seems to affect lists with multiple levels of nesting. Single-level lists appear to work fine, but once you introduce nested items with indentation, the parser fails to recognize them properly.

---
Repository: /testbed
