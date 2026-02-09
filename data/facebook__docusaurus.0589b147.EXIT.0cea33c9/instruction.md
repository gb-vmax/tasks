# Bug Report

### Describe the bug

I'm experiencing an issue with the `EXIT` constant from `unist-util-visit`. When trying to use `EXIT` to stop tree traversal, it's not working as expected. The visitor continues traversing the tree instead of stopping.

### Reproduction

```js
import { visit, EXIT } from 'unist-util-visit'

const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'first' },
    { type: 'paragraph', value: 'second' },
    { type: 'paragraph', value: 'third' }
  ]
}

visit(tree, 'paragraph', (node) => {
  console.log(node.value)
  if (node.value === 'first') {
    return EXIT  // Should stop traversal here
  }
})

// Expected: Only logs "first"
// Actual: Logs "first", "second", "third"
```

The visitor doesn't stop when `EXIT` is returned. It seems like the constant isn't being recognized properly for some reason.

### Expected behavior

Returning `EXIT` from the visitor function should immediately stop the tree traversal and not visit any remaining nodes.

---
Repository: /testbed
