# Bug Report

### Describe the bug
I'm experiencing an issue with tree traversal where the visitor function seems to be stopping prematurely when traversing AST nodes. The traversal doesn't visit all nodes in the tree as expected.

### Reproduction
```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'first' },
        { type: 'text', value: 'second' }
      ]
    },
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'third' }
      ]
    }
  ]
}

const visited = []
visit(tree, 'text', (node) => {
  visited.push(node.value)
})

// Expected: ['first', 'second', 'third']
// Actual: Only visits first node then stops
console.log(visited)
```

### Expected behavior
The visitor should traverse all matching nodes in the tree. Currently it appears to exit early and doesn't visit all the nodes it should.

Also noticed that when using reverse traversal, the starting offset seems incorrect - it's not beginning at the right position in the children array.

### System Info
- unist-util-visit version: 5.0.0
- Node version: 18.x

---
Repository: /testbed
