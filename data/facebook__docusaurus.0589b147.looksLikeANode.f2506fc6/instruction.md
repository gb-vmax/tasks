# Bug Report

### Describe the bug

I'm experiencing an issue with the AST visitor utility where it's not properly traversing tree nodes anymore. The visitor seems to be skipping nodes that should be visited, causing my transformations to fail silently.

### Reproduction

```js
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

visit(tree, 'text', (node) => {
  console.log(node.value) // This never gets called
})
```

### Expected behavior

The visitor should traverse all nodes in the tree and execute the callback for matching node types. In the example above, it should log "Hello" when visiting the text node.

### Additional context

This seems to have broken recently. My code was working fine before and I haven't changed anything on my end. The tree structure is valid and follows the unist spec correctly - each node has a `type` property and the structure is properly nested.

---
Repository: /testbed
