# Bug Report

### Describe the bug

Footnote references in GitHub Flavored Markdown are not being parsed correctly. When I use the `[^1]` syntax for footnotes in my markdown content, they don't seem to be recognized properly and the rendering is broken.

### Reproduction

```markdown
Here is some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

When parsing this markdown, the footnote call `[^1]` doesn't get processed as expected. It seems like the tokenizer is exiting too early or not continuing through the parsing flow correctly.

### Expected behavior

The footnote reference should be properly tokenized and rendered as a clickable footnote marker that links to the footnote definition at the bottom of the document.

### Additional context

This appears to affect all footnote references in GFM content. The issue seems related to how the footnote call tokenizer handles the initial parsing state - it's like the parsing stops prematurely before it can process the actual footnote identifier.

---
Repository: /testbed
