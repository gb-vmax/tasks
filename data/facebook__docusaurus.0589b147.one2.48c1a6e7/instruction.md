# Bug Report

### Describe the bug

I'm experiencing an issue with MDX processing where nested children in passthrough nodes are not being handled correctly. When using the `passThrough` option with nodes that have children, the children appear to be lost or not properly transferred to the result.

### Reproduction

```js
const mdx = require('@mdx-js/mdx')

// Create a tree with a passthrough node that has children
const tree = {
  type: 'root',
  children: [
    {
      type: 'customNode',
      children: [
        { type: 'text', value: 'child content' }
      ],
      data: { some: 'data' }
    }
  ]
}

const options = {
  passThrough: ['customNode']
}

// Process the tree
const result = await mdx.compile(tree, options)

// The children are missing from the output
// Expected: customNode should have its children preserved
// Actual: children are not present in the result
```

### Expected behavior

When processing nodes with the `passThrough` option enabled, the children of those nodes should be properly copied and included in the resulting tree structure. The shallow copy should include the processed children array.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
