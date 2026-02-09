# Bug Report

### Describe the bug

I'm experiencing an issue where custom node handlers are not being invoked when processing MDX content. Instead of using the registered handlers, the system falls back to the unknown handler even when a valid handler is defined for the node type.

### Reproduction

```js
const handlers = {
  customNode: (state, node, parent) => {
    // This handler is never called
    return processCustomNode(node);
  }
};

const tree = {
  type: 'root',
  children: [
    {
      type: 'customNode',
      value: 'test'
    }
  ]
};

// Process the tree with custom handlers
const result = compile(tree, { handlers });

// Expected: customNode handler should be called
// Actual: unknownHandler is called instead
```

### Expected behavior

When a node type has a registered handler in `state.handlers`, that handler should be invoked to process nodes of that type. The system should only fall back to the `unknownHandler` for truly unknown node types that don't have handlers defined.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to have started recently, as custom handlers were working correctly before. The handlers are being registered properly but just aren't being called during tree traversal.

---
Repository: /testbed
