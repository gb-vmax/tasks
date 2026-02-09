# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers where lazy line handling appears to be inverted. When parsing nested directive containers, lines that should be treated as lazy continuation are being marked as non-lazy, and vice versa.

### Reproduction

```markdown
::: container
Some content here
::: nested
Nested content
:::
More content
:::
```

When parsing this structure, the lazy line tracking seems backwards - lines that are part of the directive content are being incorrectly flagged, causing the parser to misinterpret the structure.

### Expected behavior

The parser should correctly identify which lines are lazy continuations within directive containers. Currently it seems like the lazy flag is being set in the opposite way from what's intended - setting `true` when it should be `false` and checking the wrong line number.

### System Info

- remark-directive version: 3.0.0
- Node version: Latest

This is affecting nested directive parsing and causing content to be incorrectly associated with parent/child containers.

---
Repository: /testbed
