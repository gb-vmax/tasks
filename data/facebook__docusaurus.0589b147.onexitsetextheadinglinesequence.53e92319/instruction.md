# Bug Report

### Describe the bug

I'm encountering an issue with setext heading parsing in markdown. When parsing setext-style headings (underlined with `=` or `-`), the heading depth is being assigned incorrectly.

### Reproduction

```markdown
Heading Level 1
===============

Heading Level 2
---------------
```

When parsing the above markdown, the heading levels are not being detected correctly. The headings seem to be getting the wrong depth values assigned to them.

### Expected behavior

- Headings underlined with `=` should be parsed as level 1 headings (depth: 1)
- Headings underlined with `-` should be parsed as level 2 headings (depth: 2)

The parser should correctly identify and assign the appropriate depth based on the underline character used.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
