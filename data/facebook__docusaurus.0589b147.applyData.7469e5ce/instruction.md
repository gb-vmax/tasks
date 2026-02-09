# Bug Report

### Describe the bug

I'm experiencing an issue with data transformation when using custom properties on nodes. When applying `hProperties` to transform a node, the properties are not being correctly assigned to the result element.

### Reproduction

```js
const node = {
  type: 'paragraph',
  data: {
    hProperties: {
      className: 'custom-class',
      id: 'my-id'
    }
  },
  children: []
}

// Transform the node
const result = applyData(node, { type: 'element', tagName: 'p', properties: {}, children: [] })

// Expected: result.properties should contain className and id
// Actual: properties may not be applied correctly
```

### Expected behavior

When a node has `hProperties` in its data, those properties should be merged into the resulting element's properties object. The transformation should correctly handle the properties regardless of the element type.

### Additional context

This seems to affect nodes that are being transformed with custom HTML properties. The issue appears when trying to add custom classes or attributes to elements during the markdown-to-HTML conversion process.

---
Repository: /testbed
