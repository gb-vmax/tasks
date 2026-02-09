# Bug Report

### Describe the bug

I'm encountering an issue with link nodes in the markdown parser. When parsing markdown links, the resulting AST nodes have an incorrect type and the children property is set to `null` instead of an empty array.

### Reproduction

```js
const processor = remark();
const ast = processor.parse('[example](https://example.com)');

// The link node has wrong structure
console.log(ast.children[0]);
// Expected: { type: 'link', url: '...', children: [] }
// Actual: { type: 'url', url: '...', children: null }
```

### Expected behavior

Link nodes should have:
- `type` property set to `"link"`
- `children` property initialized as an empty array `[]`

Currently getting `type: "url"` and `children: null` which breaks downstream processing that expects to iterate over the children array.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
