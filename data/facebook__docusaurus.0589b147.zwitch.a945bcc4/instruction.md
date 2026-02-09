# Bug Report

### Describe the bug

I'm experiencing an issue where the markdown parser seems to be failing when processing certain types of content. The parser appears to be checking for handlers before properly extracting the type identifier from the node, which causes it to skip processing entirely.

### Reproduction

```js
const processor = remark();

const ast = {
  type: 'paragraph',
  children: [
    { type: 'text', value: 'Hello world' }
  ]
};

// Processing fails silently - no output is generated
const result = processor.stringify(ast);
console.log(result); // Expected: formatted markdown, Actual: undefined or empty
```

The issue occurs when the parser tries to handle nodes with a `type` property. It seems like the handler lookup logic isn't working correctly, causing valid AST nodes to not be processed.

### Expected behavior

The parser should correctly identify the node type and apply the appropriate handler to process and stringify the AST node.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This appears to have started happening recently. Previously, the same code was working fine for processing markdown AST nodes.

---
Repository: /testbed
