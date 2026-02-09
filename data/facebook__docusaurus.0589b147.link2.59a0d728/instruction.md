# Bug Report

### Describe the bug

After a recent update, MDX link parsing appears to be broken. When parsing markdown with links, the resulting AST structure is incorrect - links are being converted to a different node type with the wrong properties.

### Reproduction

```js
const mdx = `
This is a [link](https://example.com) in markdown.
`;

const result = compile(mdx);
// Expected: AST node with type "link" and children array
// Actual: AST node with type "url" and children set to null
```

When parsing MDX content that contains standard markdown links, the compiler generates malformed AST nodes. The link nodes have:
- Wrong `type` property (should be "link")
- Missing `children` array (set to null instead of empty array)

This breaks any downstream processing that expects standard link node structures.

### Expected behavior

Link nodes should follow the standard mdast format:
- `type` should be "link"
- `children` should be an array (even if empty)

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
