# Bug Report

### Describe the bug

The footnote back reference labels are generating incorrect text. When I have footnotes in my MDX document, the "back to reference" links show the wrong reference numbers.

### Reproduction

```mdx
Here is some text with a footnote[^1].

And another reference to the same footnote[^1].

[^1]: This is the footnote content.
```

When rendered, the back reference links show:
- First reference: "Back to reference 0"
- Second reference: "Back to reference 0-1"

### Expected behavior

The back reference links should show:
- First reference: "Back to reference 1"
- Second reference: "Back to reference 1-2"

The reference index should be 1-based (starting from 1) not 0-based, since that's what users expect to see in the document.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
