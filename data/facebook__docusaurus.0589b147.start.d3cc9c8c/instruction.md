# Bug Report

### Describe the bug

Link titles with parentheses are not being parsed correctly. When I try to use a link with a title that contains parentheses, the markdown parser fails to recognize it properly.

### Reproduction

```markdown
[link text](https://example.com "title with (parens)")
```

The parser doesn't handle the opening parenthesis in the title correctly. It seems to be treating the `(` character differently than expected.

### Expected behavior

The link should be parsed correctly with the title intact, including any parentheses within the quoted title string. According to the CommonMark spec, titles can contain parentheses when properly quoted.

### Additional context

This appears to affect links where the title is enclosed in quotes and contains parentheses. The issue doesn't occur when the title has no special characters.

---
Repository: /testbed
