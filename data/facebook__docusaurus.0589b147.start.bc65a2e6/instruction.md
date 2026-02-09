# Bug Report

### Describe the bug

I'm encountering an issue with footnote definition parsing in GFM (GitHub Flavored Markdown). When processing footnote definitions, the parser appears to be closing the `gfmFootnoteDefinitionLabel` token prematurely in the tokenization flow, which is causing the structure to be incomplete or malformed.

### Reproduction

```markdown
[^1]: This is a footnote definition

Some text with a footnote reference[^1].
```

When parsing this markdown, the footnote definition label is being closed before the label content is fully processed. This affects the AST structure and downstream processing of footnote definitions.

### Expected behavior

The `gfmFootnoteDefinitionLabel` token should remain open until after the label marker (`^`) is processed and the label content begins. The token structure should properly encapsulate the entire label including the marker.

### Additional context

This seems to affect the parsing of footnote definitions specifically. The label exit is happening too early in the tokenization sequence, before `labelAtMarker` is called to process the `^` marker.

---
Repository: /testbed
