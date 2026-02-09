# Bug Report

### Describe the bug

I'm experiencing an issue with footnote back references in MDX. When a footnote is referenced multiple times in the document, the back arrow (↩) appears incorrectly on the first reference instead of only appearing on subsequent references.

### Reproduction

```mdx
Here's some text with a footnote[^1].

And here's the same footnote referenced again[^1].

[^1]: This is the footnote content.
```

When rendering this, the first back reference shows the arrow (↩) without the superscript number, but it should only show the plain arrow. The second and subsequent references should show the arrow with a superscript number (↩²).

Currently, the first reference is displaying the arrow when it shouldn't have any special formatting beyond the basic back link.

### Expected behavior

- First footnote back reference: should display just the arrow (↩) 
- Second reference: should display arrow with superscript (↩²)
- Third reference: should display arrow with superscript (↩³)
- And so on...

The logic for when to add the superscript seems to be off by one - it's checking if `rereferenceIndex > 1` when it should probably be checking a different condition.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
