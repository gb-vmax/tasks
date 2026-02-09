# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content transformation where the original node properties are being preserved instead of being replaced by the new node properties. This causes unexpected behavior when trying to transform AST nodes in remark plugins.

### Reproduction

When using a custom remark plugin that attempts to transform nodes:

```js
// Example transformation
const originalNode = {
  type: 'paragraph',
  children: [...],
  data: { originalData: true }
}

const newNode = {
  type: 'div',
  children: [...],
  data: { newData: true }
}

// After transformation, expecting newNode properties
// but getting originalNode properties instead
```

The transformed node ends up keeping properties from the original node that should have been removed, and properties from the new node are not being applied correctly.

### Expected behavior

When transforming a node, all properties from the original node should be removed first, then all properties from the new node should be applied to create a clean transformation. The resulting node should only contain properties from the new node.

### System Info

- Docusaurus version: latest
- MDX loader: @docusaurus/mdx-loader

This seems to affect any custom remark plugin that uses node transformation utilities.

---
Repository: /testbed
