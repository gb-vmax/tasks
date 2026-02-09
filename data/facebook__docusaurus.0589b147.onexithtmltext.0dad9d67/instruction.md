# Bug Report

### Describe the bug

I'm experiencing an issue with HTML text handling in markdown parsing. When parsing documents that contain HTML text nodes, the content appears to be lost or not properly captured in the resulting AST.

### Reproduction

```js
const processor = remark();
const result = processor.parse(`
<div>
Some HTML content here
</div>
`);

// The HTML text content is missing or incorrect in the parsed output
console.log(result);
```

When I parse markdown with inline HTML containing text, the text value doesn't seem to be correctly extracted from the stack. The node appears in the tree but the actual text content is empty or undefined.

### Expected behavior

The HTML text content should be properly preserved in the parsed AST node's value property, just like it works for code text and other text-based nodes.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

Has anyone else encountered this? It seems like the HTML text exit handler might not be reading from the correct position in the processing stack.

---
Repository: /testbed
