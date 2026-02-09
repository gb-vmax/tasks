# Bug Report

### Describe the bug

I'm encountering an issue with setext heading parsing where the parser crashes or produces incorrect output when processing certain markdown structures. It seems like the parser is not properly handling edge cases in setext heading underlines.

### Reproduction

```markdown
Some text
=
```

or

```markdown
Heading
-
```

When parsing markdown with setext-style headings (underlined with `=` or `-`), the parser behaves unexpectedly. The issue appears to be related to how the underline sequence is being tokenized.

### Expected behavior

The parser should correctly handle setext headings with underlines and produce the appropriate AST nodes without errors. Valid setext headings should be recognized, and edge cases should be handled gracefully.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
