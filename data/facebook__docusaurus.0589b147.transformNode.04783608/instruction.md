# Bug Report

### Describe the bug

The `transformNode` utility function is not properly transforming nodes when there are overlapping properties between the source and target nodes. Properties that exist in both `node` and `newNode` are not being updated/replaced as expected.

### Reproduction

```js
const originalNode = {
  type: 'element',
  name: 'div',
  value: 'old value',
  children: []
}

const newNode = {
  type: 'element',
  name: 'span',
  value: 'new value'
}

transformNode(originalNode, newNode)

// Expected: originalNode.name should be 'span' and value should be 'new value'
// Actual: originalNode.name is still 'div' and value is still 'old value'
```

### Expected behavior

When transforming a node, all properties from `newNode` should replace the corresponding properties in the original `node`. Properties that exist in both objects should be overwritten with the new values.

### Additional context

This affects MDX processing where AST nodes need to be transformed in place. The current behavior keeps old property values when they exist in both the original and new node, which prevents proper node transformation.

---
Repository: /testbed
