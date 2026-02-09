# Bug Report

### Describe the bug

Setext headings (underline-style headings using `=` or `-`) are not being parsed correctly. It appears that headings are being recognized in situations where they shouldn't be, or vice versa.

### Reproduction

```markdown
This is a paragraph
---

Another paragraph
===
```

When parsing the above markdown, the behavior seems inconsistent with expected setext heading rules. The underlines should create headings from the preceding text, but this doesn't seem to be working as expected.

### Expected behavior

Setext headings should be properly identified when:
1. A line of text is followed by a line of `=` (for h1) or `-` (for h2)
2. The underline meets the standard markdown criteria

The parser should correctly distinguish between setext heading underlines and other uses of these characters (like horizontal rules or list items).

### System Info
- remark version: 15.0.1

---
Repository: /testbed
