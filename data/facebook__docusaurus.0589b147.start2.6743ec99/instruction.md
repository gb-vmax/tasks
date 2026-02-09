# Bug Report

### Describe the bug

I'm experiencing an issue with link parsing in MDX where the label marker isn't being properly closed. The parser seems to be exiting the "labelLink" scope before exiting the "labelMarker" scope, which creates malformed token structures.

### Reproduction

```js
const mdx = `
This is a [link](https://example.com) in MDX.
`

// Parse the MDX content
const result = await compile(mdx)
```

When parsing markdown links, the tokenizer appears to be closing the label marker in the wrong order, causing the token tree to be incorrectly structured.

### Expected behavior

The label marker should be properly closed before the label link scope is exited. The token structure should have the labelMarker completely nested within labelLink, not partially outside of it.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to affect all link parsing in MDX documents. The issue appears to be in the `tokenizeLabelStartLink` function where the exit calls are in the wrong sequence.

---
Repository: /testbed
