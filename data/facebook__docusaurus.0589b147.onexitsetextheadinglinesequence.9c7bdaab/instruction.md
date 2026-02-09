# Bug Report

### Describe the bug

I'm experiencing an issue with setext heading parsing in the markdown processor. When parsing setext-style headings (underlined with `=` or `-`), the heading levels are being assigned incorrectly.

### Reproduction

```markdown
Heading Level 1
===============

Heading Level 2
---------------
```

When parsing the above markdown, the heading levels are reversed:
- Text underlined with `=` (which should be h1) is being parsed as h2
- Text underlined with `-` (which should be h2) is being parsed as h1

### Expected behavior

According to the CommonMark spec:
- Headings underlined with `=` should be level 1 (h1)
- Headings underlined with `-` should be level 2 (h2)

The parser should correctly assign `depth: 1` for `=` underlines and `depth: 2` for `-` underlines.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
