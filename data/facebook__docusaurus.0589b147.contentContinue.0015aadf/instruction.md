# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing where lazy continuation lines are being handled incorrectly. When a directive container has content that spans multiple lines, the parser seems to be treating continuation lines differently than expected.

### Reproduction

```markdown
::: note
This is a directive container
with multiple lines of content
that should be parsed correctly
:::
```

When parsing directive containers with multi-line content, the lazy line detection appears to be inverted - lines that should be treated as lazy continuations are being treated as non-lazy, and vice versa.

### Expected behavior

Directive containers should properly handle multi-line content with correct lazy line continuation. The parser should correctly identify which lines are lazy continuations and which are not, ensuring the content is parsed as part of the directive container block.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
