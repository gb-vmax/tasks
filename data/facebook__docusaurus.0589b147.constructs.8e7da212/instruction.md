# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser seems to be accessing array elements out of bounds and incorrectly categorizing syntax extensions. This is causing unexpected behavior when processing MDX documents with custom syntax extensions.

### Reproduction

```js
const mdx = `
# Hello World

Some content here
`;

// When using custom syntax extensions with 'add' property
const result = compile(mdx, {
  remarkPlugins: [
    // Plugin with syntax extension that has 'add' property
  ]
});
```

The issue appears when:
1. Using syntax extensions that specify where they should be added (before/after)
2. The extension list has multiple items
3. Processing tries to access beyond the array bounds

### Expected behavior

The parser should correctly process all syntax extensions without going out of bounds and should properly categorize extensions based on their `add` property (placing them before or after existing constructs as specified).

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like it could lead to crashes or undefined behavior when the array access goes beyond the valid indices. Has anyone else encountered this?

---
Repository: /testbed
