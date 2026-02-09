# Bug Report

### Describe the bug

I'm experiencing an issue with the rehype-stringify vendor code where handler dispatch is not working correctly. When processing nodes with specific types, the wrong handler is being invoked - it seems like the logic for selecting between registered handlers and the unknown handler has been inverted.

### Reproduction

```js
const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify)

const tree = {
  type: 'element',
  tagName: 'div',
  properties: {},
  children: []
}

// Process a tree with registered element handlers
const result = processor.stringify(tree)
// The unknown handler is called instead of the registered element handler
```

### Expected behavior

When a node type has a registered handler, that specific handler should be invoked. The `unknown` handler should only be called as a fallback when no registered handler exists for the given node type.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

This appears to have broken HTML serialization as nodes are not being processed with their correct handlers.

---
Repository: /testbed
