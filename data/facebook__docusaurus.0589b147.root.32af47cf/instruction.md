# Bug Report

### Describe the bug

I'm experiencing an issue with MDX root node transformation where the children array is not being wrapped properly. When processing MDX documents, the root node's children are not going through the wrapping phase, which causes problems with how content is structured in the output.

### Reproduction

```js
// Process an MDX document with multiple block-level elements
const mdx = `
# Heading

Paragraph text

Another paragraph
`;

// After transformation, the root node children are not wrapped
// Expected: children should be wrapped in appropriate container elements
// Actual: children are directly assigned without wrapping
```

### Expected behavior

The root node transformation should:
1. Process all children nodes
2. Wrap the processed children appropriately
3. Apply any data transformations
4. Patch the node with position information

The wrapping step appears to be skipped, which affects how the final HAST tree is structured.

### System Info
- MDX version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
