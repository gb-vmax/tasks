# Bug Report

### Describe the bug

I'm experiencing an issue with HTML node generation in the markdown compiler. When processing HTML content in markdown, the generated AST nodes have incorrect properties. Specifically, the node type appears to be malformed and the value is set to `null` instead of an empty string.

### Reproduction

```js
// Parse markdown with HTML content
const processor = remark();
const ast = processor.parse('<div>test</div>');

// The HTML node has wrong type and value
console.log(ast); 
// Expected: { type: "html", value: "" }
// Actual: { type: "htm", value: null }
```

### Expected behavior

HTML nodes in the AST should have:
- `type` property set to `"html"` (not `"htm"`)
- `value` property initialized as an empty string `""` (not `null`)

This is breaking downstream processing that relies on the correct node structure.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
