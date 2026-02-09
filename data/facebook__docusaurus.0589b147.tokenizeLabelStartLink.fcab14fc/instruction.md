# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where links followed by footnote syntax are being incorrectly handled. It seems like the parser is rejecting valid markdown links when they appear before a caret (`^`) character, even when footnote support is enabled.

### Reproduction

```markdown
[link text](url)^footnote
```

When parsing the above markdown, the link is not being recognized properly. The parser seems to be treating valid link syntax as invalid when a `^` character follows it.

### Expected behavior

The parser should correctly handle links that are followed by footnote markers. The link should be parsed as a valid link regardless of what character comes after it (when footnote support is available).

### Additional context

This appears to be related to how the label link tokenizer handles the interaction between link syntax and footnote markers. The behavior seems backwards - links are being rejected in cases where they should be accepted, and vice versa.

---
Repository: /testbed
