# Bug Report

### Describe the bug
Footnote definitions in GFM (GitHub Flavored Markdown) are not being parsed correctly. When trying to use footnote syntax like `[^1]: footnote text`, the parser fails to recognize it as a valid footnote definition.

### Reproduction
```markdown
Here is some text with a footnote reference[^1].

[^1]: This is the footnote definition.
```

The footnote definition is not being parsed and the reference doesn't link properly.

### Expected behavior
The parser should recognize `[^1]:` as a valid footnote definition marker and process the footnote content correctly. The `^` character (code 94) should be detected after the opening bracket to identify it as a footnote.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
