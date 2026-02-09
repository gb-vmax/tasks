# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where paragraph content is not being properly initialized. The parser seems to be entering the paragraph state at the wrong time, which causes the content structure to be incorrect.

### Reproduction

```js
const mdx = `
This is a paragraph.

Another paragraph here.
`

// Parse the MDX content
const result = compile(mdx)
// The paragraph tokens are in the wrong order
```

When parsing MDX content with multiple paragraphs, the paragraph token entry happens after the line content is already being processed instead of before. This results in an incorrect token tree structure.

### Expected behavior

The paragraph token should be entered before processing the line content, so that the token hierarchy is correct and the paragraph properly wraps its content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
