# Bug Report

### Describe the bug

I'm experiencing an issue with link parsing in markdown. When I try to create or parse links, they're not being recognized properly and the resulting AST structure seems incorrect.

### Reproduction

```js
const processor = remark();
const tree = processor.parse('[example link](https://example.com)');

// The link node has wrong structure
console.log(tree.children[0]);
// Expected: type: "link"
// Actual: type: "links" (wrong type)
// Also children is null instead of an array
```

### Expected behavior

Links should be parsed correctly with:
- `type` property set to `"link"` (not `"links"`)
- `children` property initialized as an empty array (not null)

The parsed link nodes should have the proper structure to be processed by subsequent transformers and renderers.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
