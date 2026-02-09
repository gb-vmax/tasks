# Bug Report

### Describe the bug

Strikethrough markdown syntax is not being parsed correctly. When using double tildes (`~~`) to create strikethrough text, it's not being recognized and the text appears without formatting.

### Reproduction

```markdown
This is ~~strikethrough text~~ that should have a line through it.
```

Expected the text between `~~` to be parsed as strikethrough, but it's being rendered as plain text with the tildes still visible.

### Additional context

This seems to have broken recently. The strikethrough feature was working fine before but now double tilde sequences aren't being recognized as valid strikethrough delimiters.

---
Repository: /testbed
