# Bug Report

### Describe the bug

I'm experiencing unexpected behavior when processing markdown nodes with the remark-rehype transformer. When a node has both `hProperties` and `hChildren` data properties, it's being incorrectly converted to a text node instead of an element node.

### Reproduction

```js
const node = {
  type: 'custom',
  value: 'some text',
  data: {
    hProperties: { className: 'test' },
    hChildren: [{ type: 'text', value: 'child' }]
  }
}

// Process this node with remark-rehype
// Expected: Should create an element node with the specified properties and children
// Actual: Creates a text node, ignoring hProperties and hChildren
```

### Expected behavior

When a node has both `hProperties` and `hChildren` in its data, it should be transformed into an element node (div) with those properties and children applied, not converted to a plain text node.

### Additional context

This seems to affect nodes that have a `value` property along with custom HTML properties and children specified in the data object. The transformer appears to be treating these incorrectly.

---
Repository: /testbed
