# Bug Report

### Describe the bug

I'm experiencing an issue with setext-style heading parsing where the heading depth is being assigned incorrectly. When using underline-style headings in markdown (with `=` or `-` characters), the resulting heading levels are wrong.

### Reproduction

```markdown
Heading 1
=========

Heading 2
---------
```

When parsing this markdown, the heading depths are not being set correctly. It appears that:
- Headings underlined with `=` should be level 1
- Headings underlined with `-` should be level 2

But the actual behavior doesn't match this expected pattern.

### Expected behavior

Setext headings should follow the standard markdown convention:
- Lines underlined with `=` should produce `<h1>` (depth 1)
- Lines underlined with `-` should produce `<h2>` (depth 2)

The parser should correctly identify which underline character was used and assign the appropriate heading depth.

### Additional context

This seems to be affecting the core markdown parsing functionality. The issue is consistent across different markdown inputs using setext-style headings.

---
Repository: /testbed
