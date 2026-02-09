# Bug Report

### Describe the bug

I'm experiencing an issue with the visitor function in `unist-util-visit` where the parent node and index values being passed to the visitor callback appear to be incorrect. When traversing a syntax tree, the visitor receives the wrong parent node - it seems to be getting the grandparent instead of the actual parent node.

### Reproduction

```js
import { visit } from 'unist-util-visit'

const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'Hello' }
      ]
    }
  ]
}

visit(tree, 'text', (node, index, parent) => {
  console.log('Node:', node.value)
  console.log('Parent type:', parent?.type)
  console.log('Index:', index)
  // Expected: parent.type should be 'paragraph'
  // Actual: parent.type is 'root' (grandparent)
})
```

### Expected behavior

When visiting a text node that is a child of a paragraph node, the visitor callback should receive:
- The text node as `node`
- The paragraph node as `parent`
- The correct index of the text node within the paragraph's children array

Instead, it appears to be passing the grandparent node and an incorrect index value.

### System Info

- unist-util-visit version: 5.0.0
- Node.js version: Latest

This is breaking my tree transformation logic that relies on accurate parent references. Any help would be appreciated!

---
Repository: /testbed
