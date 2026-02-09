# Bug Report

### Describe the bug

Footnote references with escaped characters are not being parsed correctly. When a footnote call contains backslash-escaped characters, the parser seems to get stuck or fail to properly recognize the footnote.

### Reproduction

```markdown
This is a footnote with an escaped bracket[^foo\]bar].

[^foo\]bar]: The footnote definition
```

When parsing this markdown, the footnote reference is not being recognized properly. It appears that after encountering an escape sequence, the parser doesn't continue processing the footnote call correctly.

### Expected behavior

Footnote calls containing escaped characters (like `\]`, `\[`, or `\\`) should be parsed correctly and matched with their corresponding definitions. The escape sequences should be handled transparently within the footnote identifier.

### Additional context

This seems to affect GFM-style footnotes specifically. Regular footnotes without escape sequences work fine, but as soon as you include a backslash escape within the footnote identifier, things break down.

---
Repository: /testbed
