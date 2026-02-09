# Bug Report

### Describe the bug

I'm encountering an issue with inline code rendering in GFM tables. When using inline code (backticks) inside table cells that contain escaped pipe characters, only the first escaped character is being unescaped instead of all of them.

### Reproduction

```markdown
| Column 1 | Column 2 |
|----------|----------|
| `foo \| bar \| baz` | test |
```

When this is parsed, the inline code should display as `foo | bar | baz`, but instead it's showing `foo | bar \| baz` - only the first escaped pipe is being handled correctly.

### Expected behavior

All escaped pipe characters (`\|`) and backslashes (`\\`) within inline code in table cells should be unescaped properly, not just the first occurrence.

### Additional context

This seems to affect any inline code in tables where multiple escape sequences are present. The issue appears to be specific to the table context - inline code outside of tables works fine with escaped characters.

---
Repository: /testbed
