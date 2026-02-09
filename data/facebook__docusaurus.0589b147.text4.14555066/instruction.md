# Bug Report

### Describe the bug

I'm experiencing an issue with text node generation in the markdown parser. When parsing markdown content, text nodes are being created with incorrect type and value properties. Instead of getting proper text nodes with empty strings, I'm seeing nodes with type "txt" and a space character as the value.

### Reproduction

```js
// Parse any markdown with text content
const ast = parse('some text here')

// Inspect the generated text nodes
console.log(ast.children[0])
// Expected: { type: "text", value: "" }
// Actual: { type: "txt", value: " " }
```

This affects any markdown parsing operation that involves text nodes, causing downstream processors to fail or behave unexpectedly since they're looking for nodes with type "text" but getting "txt" instead.

### Expected behavior

Text nodes should have:
- `type` property set to `"text"` (not `"txt"`)
- `value` property initialized to empty string `""` (not a space `" "`)

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
