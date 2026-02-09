# Bug Report

### Describe the bug

I'm experiencing an issue with object property enumeration after a recent update. When using the library to traverse AST nodes, properties that should be accessible are not being copied/enumerated correctly.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      data: { id: 1 },
      children: []
    }
  ]
}

// After visiting nodes, properties seem to be missing or incorrectly enumerated
visit(tree, 'paragraph', (node) => {
  console.log(node.data) // Expected: { id: 1 }, but properties may not be accessible
})
```

### Expected behavior

All object properties should be properly enumerated and accessible when traversing the tree structure. The internal property copying mechanism should correctly handle both object and function types.

### System Info
- Node version: 18.x
- Library version: Latest

---
Repository: /testbed
