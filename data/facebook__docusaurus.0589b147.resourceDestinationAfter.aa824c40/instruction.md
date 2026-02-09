# Bug Report

### Describe the bug

I'm encountering an issue with markdown link parsing where whitespace handling in resource destinations appears to be broken. Links that contain spaces or line breaks in their URLs are not being parsed correctly.

### Reproduction

```markdown
[link text](https://example.com/path with spaces)

[another link](https://example.com/path
with-linebreak)
```

When parsing these markdown links, the parser seems to be handling whitespace incorrectly in the resource destination part of the link syntax. The behavior changed recently and links that should be valid (or invalid) are now being processed in the opposite way.

### Expected behavior

The parser should correctly identify when whitespace appears in a resource destination and handle it according to the markdown spec. Currently, the whitespace detection logic seems inverted - it's calling the wrong handler function depending on whether whitespace is present or not.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
