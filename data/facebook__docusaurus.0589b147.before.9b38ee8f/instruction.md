# Bug Report

### Describe the bug

After a recent update, setext headings (underlined headings using `===` or `---`) are not being parsed correctly. The parser seems to hang or fail when encountering these heading styles.

### Reproduction

```markdown
This is a heading
=================

This is another heading
-----------------------
```

When trying to parse markdown with setext-style headings, the parser doesn't complete properly. The heading content appears to be consumed but the parsing flow breaks.

### Expected behavior

Setext headings should be parsed correctly and converted to the appropriate heading nodes in the AST. Both `=` (level 1) and `-` (level 2) underline styles should work as expected.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
