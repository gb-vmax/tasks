# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content transformation where node properties aren't being properly replaced during AST transformations. When transforming nodes in remark plugins, the original node properties remain instead of being replaced with the new node's properties.

### Reproduction

```js
// In a remark plugin
const originalNode = {
  type: 'paragraph',
  children: [...],
  data: { some: 'value' }
}

const newNode = {
  type: 'div',
  children: [...],
  data: { other: 'value' }
}

transformNode(originalNode, newNode)

// Expected: originalNode should now have newNode's properties
// Actual: originalNode keeps its original properties or has incorrect values
```

### Expected behavior

When calling `transformNode()`, the original node should be mutated to have all the properties from the new node. The transformation should replace the old node's properties with the new node's properties while maintaining the same object reference.

### Additional context

This affects MDX processing where we need to transform AST nodes in place. The node reference needs to stay the same but the properties should be completely replaced with the new node's properties.

---
Repository: /testbed
