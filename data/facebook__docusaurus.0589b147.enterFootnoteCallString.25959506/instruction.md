# Bug Report

### Describe the bug

I'm encountering an issue with footnote rendering in GFM (GitHub Flavored Markdown). When using footnote references in markdown text, the footnote labels are appearing empty or not rendering correctly.

### Reproduction

```markdown
Here is some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

When this markdown is parsed, the footnote reference shows up but the label/identifier seems to be missing or corrupted. The footnote call appears to be losing its content during the parsing process.

### Expected behavior

The footnote reference should display correctly with its label (e.g., `[^1]`) and link properly to the corresponding footnote definition.

### Additional context

This seems to affect all footnote references in the document. The footnote definitions themselves appear to parse fine, but the inline references are broken.

---
Repository: /testbed
