# Bug Report

### Describe the bug

The footnote back reference labels are showing incorrect numbering. When you have footnotes in your MDX document, the "Back to reference" links are off by one - they're displaying reference numbers that are one higher than they should be.

### Reproduction

```mdx
Here's some text with a footnote[^1].

And another footnote[^2].

[^1]: First footnote
[^2]: Second footnote
```

When rendered, the back reference links show:
- "Back to reference 2" (should be "Back to reference 1")
- "Back to reference 3" (should be "Back to reference 2")

### Expected behavior

The back reference labels should correctly match the actual footnote reference numbers in the document. For the first footnote, it should say "Back to reference 1", not "Back to reference 2".

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
