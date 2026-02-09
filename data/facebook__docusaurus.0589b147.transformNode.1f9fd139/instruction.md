# Bug Report

### Describe the bug

I'm experiencing an issue with MDX node transformations where not all properties are being properly transferred between nodes. It seems like some node properties are being skipped during the transformation process, which leads to incomplete node objects.

### Reproduction

When transforming AST nodes in MDX files, the transformed nodes are missing certain properties. This happens when using the `transformNode` utility function with remark plugins.

```js
// Example transformation
const originalNode = {
  type: 'element',
  tagName: 'div',
  properties: {},
  children: []
}

const newNode = {
  type: 'element',
  tagName: 'span',
  properties: { className: 'test' },
  children: []
}

transformNode(originalNode, newNode)
// Some properties from newNode don't get copied to originalNode
```

### Expected behavior

All properties from the new node should be copied to the original node, and all old properties should be removed. The transformation should be complete and not skip any properties.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing issues with custom remark plugins that rely on complete node transformations. Any help would be appreciated!

---
Repository: /testbed
