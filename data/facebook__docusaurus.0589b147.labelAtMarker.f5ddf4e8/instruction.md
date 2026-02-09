# Bug Report

### Describe the bug

Footnote definitions are not being parsed correctly in markdown. The parser seems to be accepting invalid footnote syntax and rejecting valid ones.

### Reproduction

```markdown
[^1]: This is a valid footnote definition
```

When trying to parse this standard GFM footnote definition, it's not being recognized. However, invalid syntax without the caret (`^`) character is being incorrectly accepted.

### Expected behavior

The parser should correctly identify footnote definitions that start with `[^` followed by an identifier and `]:`. Currently it appears to be doing the opposite - rejecting valid footnotes and accepting invalid ones.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
