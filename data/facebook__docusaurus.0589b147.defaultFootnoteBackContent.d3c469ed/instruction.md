# Bug Report

### Describe the bug

I'm experiencing an issue with footnote back-references in MDX documents. When a footnote is referenced multiple times in the document, the superscript numbering on the back-reference arrows appears to be off by one.

### Reproduction

```mdx
Here is some text with a footnote[^1].

More text referencing the same footnote again[^1].

[^1]: This is the footnote content.
```

When rendered, the first back-reference arrow shows a superscript "1" when it shouldn't show any superscript at all (since it's the first reference). The second back-reference shows "2" instead of "1".

### Expected behavior

- The first back-reference arrow (↩) should not have a superscript number
- The second back-reference arrow should show superscript "1" 
- The third would show "2", and so on

Currently it seems like the numbering is starting at 1 instead of only appearing from the second reference onwards.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
