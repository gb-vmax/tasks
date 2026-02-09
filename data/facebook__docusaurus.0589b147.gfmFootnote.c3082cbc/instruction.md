# Bug Report

### Describe the bug

Footnote references in markdown are not being parsed correctly. When trying to use GFM-style footnotes with the `[^1]` syntax, they're not being recognized or rendered properly.

### Reproduction

```markdown
Here is some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

When parsing the above markdown, the footnote reference `[^1]` is not being detected and the footnote definition is not being linked correctly.

### Expected behavior

The parser should correctly identify and tokenize footnote references (e.g., `[^1]`) and footnote definitions (e.g., `[^1]: content`) according to GFM spec. The footnote reference should be linked to its corresponding definition.

### Additional context

This seems to have started happening recently. The footnote syntax was working fine before but now the references aren't being picked up at all during parsing.

---
Repository: /testbed
