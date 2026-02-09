# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM block parsing where the `data.estree` property is being set incorrectly on MDX ESM nodes. When processing ESM blocks in MDX files, the estree data appears to be attached to nodes even when the estree is undefined or not present, and it seems like the wrong node in the stack is being referenced.

### Reproduction

```js
// Create an MDX file with an ESM block
const mdxContent = `
export const foo = 'bar'

# Hello World
`

// Parse the MDX content
const result = await compile(mdxContent)

// The mdxjsEsm node's data.estree is incorrectly set
// Expected: data.estree should only be set when estree exists
// Actual: data.estree is being set when it shouldn't be
```

### Expected behavior

- The `data.estree` property should only be attached to the mdxjsEsm node when the estree is actually present/truthy
- The correct node from the stack should be used when setting properties

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken ESM block handling in MDX files. The logic for determining when to attach estree data appears to be inverted.

---
Repository: /testbed
