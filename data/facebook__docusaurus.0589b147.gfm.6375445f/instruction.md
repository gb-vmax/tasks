# Bug Report

### Describe the bug

After a recent update, footnote syntax in markdown is no longer being parsed correctly. Footnotes that were previously working are now being completely ignored and rendered as plain text.

### Reproduction

```markdown
Here is some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

Expected: The footnote reference should be converted to a superscript link, and the footnote content should appear at the bottom of the document.

Actual: The text `[^1]` appears as literal text in the output, and the footnote definition is not processed.

### Steps to reproduce
1. Create a markdown document with footnote syntax
2. Process it with remark-gfm
3. Observe that footnotes are not rendered

### Expected behavior
Footnotes should be parsed and rendered according to GitHub Flavored Markdown spec. The reference should link to the footnote definition.

### Additional context
This was working fine in previous versions. It seems like footnote processing has stopped working entirely. Other GFM features like tables and task lists still work as expected.

---
Repository: /testbed
