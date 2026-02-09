# Bug Report

### Describe the bug

I'm experiencing an issue with MDX processing where empty arrays are being spread into the output, causing unexpected behavior in the rendered content. It seems like the code is pushing empty arrays even when there's nothing to add, which shouldn't happen.

### Reproduction

When processing MDX content with specific node structures, the output includes empty spreads that shouldn't be there. This affects the final rendered structure.

```js
// Processing MDX content with mixed node types
const mdxContent = `
# Title

Some text

<Component />

More text
`;

// The resulting cleanChildren array contains empty array spreads
// Expected: only actual children nodes
// Actual: includes empty array elements
```

### Expected behavior

The processing should only add actual child nodes to the output. Empty queues should not be spread into the result array.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
