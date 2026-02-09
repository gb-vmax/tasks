# Bug Report

### Describe the bug

I'm encountering an issue with setext heading underlines in markdown parsing. When processing setext headings (headings underlined with `=` or `-`), the parser seems to be handling whitespace and the underline sequence incorrectly.

### Reproduction

```markdown
Heading Text
============  
```

or

```markdown
Another Heading
---------------
```

When parsing setext-style headings with underlines, the output doesn't match what's expected. The heading structure appears to be malformed in the resulting AST.

### Expected behavior

Setext headings should be properly parsed with the underline sequence correctly tokenized. The heading line sequence should exit at the appropriate point and trailing whitespace should be handled correctly.

### Additional context

This seems to affect how the tokenizer processes the sequence of underline characters and any whitespace that follows them. The heading recognition works, but the internal token structure isn't being built correctly.

---
Repository: /testbed
