# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing in markdown content. When I have directives that span multiple lines, the parser seems to be handling them incorrectly. Specifically, lazy continuation lines are being processed when they shouldn't be (or vice versa).

### Reproduction

```markdown
:::note
This is a directive
with multiple lines
:::
```

When parsing this kind of multi-line directive, the behavior is inconsistent. Sometimes continuation lines are treated as part of the directive when they should be separate, and other times they're split when they should be together.

### Expected behavior

Multi-line directives should be parsed correctly with proper handling of line continuations. The parser should correctly identify which lines belong to the directive block and which don't.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
