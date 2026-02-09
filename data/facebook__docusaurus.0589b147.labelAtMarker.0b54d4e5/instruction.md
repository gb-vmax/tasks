# Bug Report

### Describe the bug

Footnote definitions are not being parsed correctly. When trying to use footnote syntax in markdown, the footnotes aren't being recognized and rendered properly.

### Reproduction

```markdown
Here is some text with a footnote reference[^1].

[^1]: This is the footnote definition.
```

When parsing this markdown, the footnote definition `[^1]:` is not being recognized. It seems like the parser is looking for the wrong character code when checking for the caret symbol (`^`) that denotes a footnote.

### Expected behavior

The footnote definition should be parsed correctly and the footnote should be linked to its reference in the text. The parser should recognize `[^` as the start of a footnote definition.

### Additional context

This appears to affect all footnote definitions. Regular footnote references in the text might work, but the definitions themselves are not being processed.

---
Repository: /testbed
