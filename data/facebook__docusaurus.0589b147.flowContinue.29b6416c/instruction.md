# Bug Report

### Describe the bug

I'm experiencing an issue with MDX document parsing where the document flow state handling seems to be incorrect. When processing markdown content that ends with certain flow constructs, the document structure gets corrupted or produces unexpected output.

### Reproduction

```js
const mdx = `
# Heading

Some content here

- List item 1
- List item 2
`

// Parse the MDX content
const result = await compile(mdx)
```

When the document ends with flow content (like lists, blockquotes, or code blocks), the parsing doesn't complete properly. The issue appears to be related to how the document flow state is being finalized.

### Expected behavior

The MDX content should parse correctly regardless of what type of flow content appears at the end of the document. The document structure should be properly closed and all tokens should be in the correct order.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
