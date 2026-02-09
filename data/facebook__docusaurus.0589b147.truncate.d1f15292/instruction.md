# Bug Report

### Describe the bug

When using the blog truncate feature, content after the truncate marker is being included in the excerpt. The truncated content appears to have extra whitespace or the split isn't working as expected.

### Reproduction

```md
This is the excerpt content that should appear.

<!--truncate-->

This is the full content that should NOT appear in the excerpt.
```

When processing this blog post, the excerpt includes content beyond the `<!--truncate-->` marker or has unexpected behavior with the content split.

### Expected behavior

Only the content before the `<!--truncate-->` marker should be included in the excerpt. Everything after the marker should be excluded from the truncated version.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
