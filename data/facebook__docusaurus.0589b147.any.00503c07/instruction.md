# Bug Report

### Describe the bug

I'm encountering an issue with the `unist-util-visit` utility where visiting nodes with multiple test conditions is not working as expected. When I provide multiple test functions to filter nodes, the visitor seems to always match nodes regardless of whether they actually satisfy any of the conditions.

### Reproduction

```js
import {visit} from 'unist-util-visit'

const tree = {
  type: 'root',
  children: [
    {type: 'paragraph', value: 'test'},
    {type: 'heading', value: 'title'},
    {type: 'list', children: []}
  ]
}

const visited = []

// Should only visit 'paragraph' or 'heading' nodes
visit(tree, ['paragraph', 'heading'], (node) => {
  visited.push(node.type)
})

console.log(visited)
// Expected: ['paragraph', 'heading']
// Actual: ['paragraph', 'heading', 'list', 'root'] (visits ALL nodes)
```

The visitor is matching every single node in the tree even though I've specified it should only match nodes of type 'paragraph' or 'heading'. It seems like the test conditions are being completely ignored.

### Expected behavior

The visitor should only traverse and execute the callback on nodes that match at least one of the provided test conditions. Nodes that don't match any condition should be skipped.

### System Info
- Version: 5.0.0
- Node.js: v18.x

---
Repository: /testbed
