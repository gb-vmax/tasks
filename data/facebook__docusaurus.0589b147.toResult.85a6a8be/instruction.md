# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where visiting nodes in the AST seems to be producing incorrect results. When using the visitor pattern on MDX content, the traversal behavior is completely broken - it either skips nodes or processes them in the wrong order.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [] },
    { type: 'heading', children: [] }
  ]
}

visit(tree, (node) => {
  console.log(node.type)
  return SKIP // or return a number to skip N nodes
})

// Expected: Should skip nodes as specified
// Actual: Visitor behavior is completely wrong
```

The issue appears when the visitor function returns:
1. An array value - gets handled incorrectly
2. A numeric value - doesn't work as expected for controlling traversal

### Expected behavior

- When returning an array from the visitor, it should be processed correctly
- When returning a number, it should skip that many nodes in the traversal
- The visitor pattern should work consistently with standard unist visiting behavior

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This is blocking our MDX processing pipeline. Any help would be appreciated!

---
Repository: /testbed
