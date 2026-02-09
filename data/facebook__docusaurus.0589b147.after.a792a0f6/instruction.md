# Bug Report

### Describe the bug

I'm encountering an issue with setext-style headings (underlined with `=` or `-`) in markdown parsing. When a setext heading has content after the underline on the same line, it's not being properly rejected and instead seems to be accepted as a valid heading.

### Reproduction

```markdown
Heading Text
============ some extra text here
```

The above should **not** be recognized as a valid setext heading because there's content after the underline sequence. According to the CommonMark spec, setext heading underlines must be followed only by optional spaces and then a line ending or EOF.

Another example:
```markdown
My Heading
------extra
```

### Expected behavior

Setext headings with any non-whitespace content after the underline sequence should be rejected and treated as regular paragraph text instead. The parser should only accept setext headings when the underline is followed by:
- End of file (null)
- Line ending characters
- Optional whitespace before line ending/EOF

### System Info
- Remark version: 15.0.1
- Using the vendored micromark tokenizer

---
Repository: /testbed
