# Bug Report

### Describe the bug

I'm encountering an issue with link parsing when using the `^` character (caret) in markdown. It seems like links followed by a caret are not being parsed correctly, and the behavior appears to be inverted from what it should be.

### Reproduction

```markdown
[test link](https://example.com)^
```

When parsing this markdown, the link is not being recognized properly when followed by a `^` character. The parser seems to be rejecting valid links in certain cases involving the caret symbol.

### Expected behavior

Links should be parsed correctly regardless of whether they're followed by a `^` character, unless footnote support is explicitly disabled. The current behavior seems backwards - links are being rejected when they should be accepted and vice versa.

### System Info
- remark version: 15.0.1
- Parser: micromark-core-commonmark

This might be related to footnote handling logic, but I'm not entirely sure. Any help would be appreciated!

---
Repository: /testbed
