# Bug Report

### Describe the bug

I'm encountering an issue with markdown link title parsing. When I use single quotes (`'`) to wrap link titles, they are no longer being recognized or parsed correctly. This appears to have broken after a recent update.

### Reproduction

```markdown
[link text](https://example.com 'title with single quotes')
```

The above markdown should be valid according to CommonMark spec, but the title is not being parsed properly.

### Expected behavior

Single-quoted link titles should be recognized and parsed the same way as double-quoted titles. According to the CommonMark specification, all three of these should be valid:

```markdown
[link](url "double quotes")
[link](url 'single quotes')
[link](url (parentheses))
```

Currently, only double quotes and parentheses seem to work.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
