# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM block parsing where the estree data is being attached to nodes incorrectly. When processing MDX files with ESM imports/exports, the resulting AST nodes don't have the expected estree data structure, or the data is being added when it shouldn't be.

### Reproduction

```js
// Example MDX content with ESM
export const foo = 'bar'

# Hello World
```

When parsing this MDX content, the mdxjsEsm node should contain the estree data from the parsed ESM block, but it seems like the logic for when to attach this data might be inverted or the wrong node is being referenced.

### Expected behavior

The mdxjsEsm AST node should properly contain the estree data structure when the token has estree information available. The data should be attached to the correct node in the stack.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
