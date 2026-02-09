# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where position mappings seem to be off by one. When working with MDX content that contains JSX expressions or components, the source positions reported in the AST don't align correctly with the actual content.

### Reproduction

```js
// Parse MDX content with JSX expression
const mdxContent = `
# Hello

<Component prop="value" />

Some text with {expression} here
`

// The position data for tokens appears to be shifted
// Expected positions don't match actual character offsets in the source
```

### Expected behavior

Position mappings should accurately reflect the character positions in the original MDX source. When I query a position from the parsed result, it should point to the correct location in the source text.

Currently, it seems like the positions are being calculated before the value is updated rather than after, causing everything to be offset incorrectly.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
