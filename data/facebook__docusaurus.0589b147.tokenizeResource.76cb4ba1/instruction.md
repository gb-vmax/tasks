# Bug Report

### Describe the bug

Markdown link parsing is broken when the URL contains certain characters. Links with titles that use quotes (single or double) or parentheses are not being recognized correctly.

### Reproduction

```markdown
[link text](https://example.com "title with quotes")
[another link](https://example.com 'single quotes')
[nested](https://example.com (parentheses))
```

When parsing these markdown links, they are not being processed as expected. The link parser seems to be rejecting valid markdown syntax.

### Expected behavior

All three link formats should be parsed correctly:
- Links with double-quoted titles: `[text](url "title")`
- Links with single-quoted titles: `[text](url 'title')`
- Links with parenthetical titles: `[text](url (title))`

These are all valid markdown link syntaxes according to the CommonMark spec.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
