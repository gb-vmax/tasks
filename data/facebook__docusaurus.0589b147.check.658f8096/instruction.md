# Bug Report

### Describe the bug

I'm experiencing an issue with the AST visitor utility where non-node values are being incorrectly processed during tree traversal. The visitor seems to be accepting values that don't match the expected node structure, which causes unexpected behavior when filtering or visiting specific node types.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'text' },
    'invalid-node-string',  // This shouldn't be visited
    { type: 'heading', depth: 1 }
  ]
}

visit(tree, 'paragraph', (node) => {
  console.log(node)
})

// The visitor incorrectly processes non-node values
// Expected: Only actual node objects should be visited
// Actual: Non-node values are also being processed
```

### Expected behavior

The visitor should only traverse and process actual node objects that have the proper structure (with `type` property). String values or other primitives in the tree should be ignored or filtered out before being passed to the test function.

### Additional context

This seems to affect tree structures that might contain mixed content or malformed nodes. The visitor should be more strict about validating node structure before attempting to process them.

---
Repository: /testbed
