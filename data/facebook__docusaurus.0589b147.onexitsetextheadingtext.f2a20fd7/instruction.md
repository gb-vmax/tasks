# Bug Report

### Describe the bug

I'm encountering an issue with setext-style headings in markdown parsing. When processing setext headings (headings underlined with `=` or `-`), the parser seems to get stuck or doesn't properly handle the heading text in certain cases.

### Reproduction

```markdown
This is a setext heading
========================

Some content here.

Another heading
---------------
```

When parsing markdown with setext-style headings like above, the heading text doesn't seem to be processed correctly. The parser appears to have issues with the line ending handling after the heading text.

### Expected behavior

Setext headings should be parsed correctly with their text content properly captured, regardless of the underline style used (`=` for h1, `-` for h2).

### Additional context

This seems to affect setext headings specifically - ATX-style headings (using `#` symbols) work fine. The issue appears to be related to how the parser handles the transition between the heading text and the underline sequence.

---
Repository: /testbed
