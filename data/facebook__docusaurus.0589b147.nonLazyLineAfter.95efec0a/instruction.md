# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers where lazy continuation lines are not being handled correctly. When using container directives with content that spans multiple lines, the parser seems to be treating lines incorrectly in terms of lazy continuation.

### Reproduction

```markdown
:::note
This is a container directive
with multiple lines of content
that should be parsed correctly
:::
```

When parsing the above directive container, the lines inside the container are being marked with the wrong lazy continuation status. This causes the parser to incorrectly interpret which lines belong to the container and which don't.

### Expected behavior

Lines within a directive container should be properly tracked for lazy continuation. The parser should correctly identify whether a line is a lazy continuation or not, ensuring that multi-line content within directives is parsed as expected.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems to have broken after a recent update. The directive container parsing was working fine before.

---
Repository: /testbed
