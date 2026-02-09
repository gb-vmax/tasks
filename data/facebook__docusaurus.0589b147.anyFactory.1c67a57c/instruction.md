# Bug Report

### Describe the bug

I'm experiencing an issue with node filtering when using multiple test conditions. When I provide an array of test functions to filter nodes, the behavior seems inverted - nodes that should match are being skipped, and nodes that shouldn't match are being visited.

### Reproduction

```js
import {visit} from 'unist-util-visit'

const tree = {
  type: 'root',
  children: [
    {type: 'paragraph', value: 'text'},
    {type: 'heading', value: 'title'},
    {type: 'code', value: 'snippet'}
  ]
}

const visited = []

// Visit nodes that are either 'paragraph' or 'heading'
visit(tree, ['paragraph', 'heading'], (node) => {
  visited.push(node.type)
})

console.log(visited)
// Expected: ['paragraph', 'heading']
// Actual: ['code'] or similar incorrect result
```

When passing an array of node types to match against, the visitor seems to be doing the opposite of what's expected. It's visiting nodes that DON'T match any of the provided types instead of the ones that DO match.

### Expected behavior

The visitor should traverse and execute the callback only on nodes that match at least one of the provided test conditions. If I specify `['paragraph', 'heading']`, it should visit paragraph and heading nodes, not other node types.

### System Info
- unist-util-visit version: 5.0.0
- Node.js version: 18.x

---
Repository: /testbed
