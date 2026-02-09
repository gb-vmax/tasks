# Bug Report

### Describe the bug

I'm encountering an issue with Markdown link parsing where links with resources are not being parsed correctly. It seems like the parser is failing to properly recognize the opening and closing parentheses in link syntax.

### Reproduction

```markdown
[link text](https://example.com)
```

When trying to parse standard Markdown links, the parser appears to be checking for the wrong character codes. Links that should be valid are either not being recognized or are being parsed incorrectly.

### Expected behavior

Standard Markdown link syntax like `[text](url)` should be parsed correctly. The opening parenthesis (character code 40) should mark the start of the resource, and the closing parenthesis (character code 41) should properly close it.

Currently it seems like these character codes might be swapped or checked incorrectly, causing link parsing to fail.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
