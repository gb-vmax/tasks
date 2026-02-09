# Bug Report

### Describe the bug

I'm experiencing an issue with setext heading parsing in remark. When parsing markdown with setext-style headings (underlined with `=` or `-`), the heading depth is being set incorrectly.

### Reproduction

```markdown
Heading Level 1
===============

Heading Level 2
---------------
```

When parsing the above markdown, the heading depths are not being assigned correctly. It seems like the parser is checking for the wrong character code and accessing the wrong position in the stack.

### Expected behavior

- Headings underlined with `=` should be parsed as level 1 headings (depth: 1)
- Headings underlined with `-` should be parsed as level 2 headings (depth: 2)

The parser should correctly identify which underline character is being used and set the appropriate depth.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
