# Bug Report

### Describe the bug

I'm experiencing an issue with the `visit` function where the parent node and index values passed to the visitor callback are incorrect. The parent being passed seems to be off by one level in the tree hierarchy, and the index is also shifted by 1.

### Reproduction

```js
import {visit} from 'unist-util-visit'

const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        {type: 'text', value: 'hello'},
        {type: 'text', value: 'world'}
      ]
    }
  ]
}

visit(tree, 'text', (node, index, parent) => {
  console.log('Node:', node.value)
  console.log('Index:', index)
  console.log('Parent type:', parent?.type)
})
```

### Expected behavior

When visiting text nodes, the callback should receive:
- `index`: 0 for "hello", 1 for "world" 
- `parent`: the paragraph node containing the text nodes

### Actual behavior

The parent and index values don't match what I expect. The parent seems to be pointing to the wrong node in the tree, and the index is off by one.

This is causing issues in my code where I need to access sibling nodes or perform operations based on the node's position within its parent.

---
Repository: /testbed
