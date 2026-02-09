# Bug Report

### Describe the bug

Footnote references in markdown are not being parsed correctly. When trying to use GFM-style footnote syntax like `[^1]`, the parser seems to terminate early and doesn't properly recognize the footnote call.

### Reproduction

```markdown
Here is some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

When parsing this markdown, the footnote reference is not being detected or linked to the footnote definition. The parser appears to exit prematurely during the tokenization of the footnote call marker.

### Expected behavior

The footnote reference `[^1]` should be properly parsed and connected to its corresponding footnote definition. The output should render the footnote as a superscript link that connects to the footnote content at the bottom of the document.

### Additional context

This seems to have broken recently. Footnotes were working fine before, but now they're just being rendered as plain text instead of being processed as footnote references.

---
Repository: /testbed
