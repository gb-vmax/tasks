# Bug Report

### Describe the bug

I'm experiencing an issue with footnote parsing in markdown documents. When using footnote references in the text, they're not being processed correctly - the footnote calls appear to be getting mixed up with footnote definitions.

### Reproduction

```markdown
This is some text with a footnote reference[^1].

[^1]: This is the footnote definition.
```

When parsing this markdown, the footnote reference `[^1]` in the text is not being handled properly. It seems like the parser is confusing footnote calls (references in the text) with footnote definitions (the actual footnote content at the bottom).

### Expected behavior

Footnote references in the text should be parsed as footnote calls, and the footnote content at the bottom should be parsed as footnote definitions. These are two distinct elements that should be handled separately.

### Additional context

This appears to be related to the GFM (GitHub Flavored Markdown) footnote extension. The parsing seems to have gotten confused between the enter/exit handlers for footnote calls vs footnote definitions.

---
Repository: /testbed
