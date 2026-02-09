# Bug Report

### Describe the bug

I'm encountering an issue with setext heading parsing where the underline sequence isn't being recognized correctly. It seems like the tokenizer is not entering the proper state when processing setext heading underlines (the `===` or `---` lines under headings).

### Reproduction

```markdown
This is a heading
=================

Another heading
---------------
```

When parsing markdown with setext-style headings (underlined with `=` or `-`), the parser doesn't seem to handle them properly. The heading line sequence state is not being entered correctly, which causes the setext headings to not be recognized as headings at all.

### Expected behavior

Setext headings should be parsed correctly:
- Lines underlined with `===` should be treated as level 1 headings
- Lines underlined with `---` should be treated as level 2 headings

The tokenizer should properly enter the `setextHeadingLineSequence` state before processing the underline characters.

### System Info
- remark version: 15.0.1
- Environment: Node.js

---
Repository: /testbed
