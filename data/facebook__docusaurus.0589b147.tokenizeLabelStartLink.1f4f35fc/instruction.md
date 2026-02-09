# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where links followed by a caret character (`^`) are not being processed correctly. The parser seems to be rejecting valid link syntax when a caret appears immediately after the closing bracket.

### Reproduction

```markdown
[example link]^
```

When parsing this markdown, the link is not recognized/tokenized properly. The caret character after the link bracket seems to interfere with the link parsing logic.

### Expected behavior

The link should be parsed normally regardless of what character follows it. A caret character appearing after a link closing bracket shouldn't affect the link tokenization.

### Additional context

This seems related to the footnote support logic. The behavior changed recently and now links that would previously parse correctly are being rejected when followed by `^`.

---
Repository: /testbed
