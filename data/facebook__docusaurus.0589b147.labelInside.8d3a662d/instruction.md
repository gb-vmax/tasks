# Bug Report

### Describe the bug

Footnote definitions with empty labels (e.g., `[^]:`) are being accepted when they should be rejected. According to GFM spec, a footnote definition must have at least one character in the label, but the parser is currently allowing empty labels to pass through.

### Reproduction

```markdown
[^]: This is a footnote with an empty label
```

This should be rejected as invalid syntax, but it's currently being parsed as a valid footnote definition.

### Expected behavior

The parser should reject footnote definitions that have empty labels (no content between `[^` and `]`). Only footnote definitions with at least one character in the label should be accepted, like:

```markdown
[^1]: Valid footnote
[^note]: Also valid
```

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
