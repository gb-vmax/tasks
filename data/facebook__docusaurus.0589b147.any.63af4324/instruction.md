# Bug Report

### Describe the bug

I'm experiencing an issue with the visitor pattern when using multiple test conditions. When I provide an array of test functions to filter nodes, the first matching condition in the array is being skipped and never evaluated correctly.

### Reproduction

```js
// Example: trying to visit nodes that match either 'heading' or 'paragraph'
visit(tree, ['heading', 'paragraph'], (node) => {
  console.log(node.type);
});

// Expected: Should visit both heading and paragraph nodes
// Actual: Only paragraph nodes are visited, heading nodes are skipped
```

The problem occurs when using an array of multiple conditions. If I use a single condition, it works fine, but with multiple conditions the first one in the array doesn't get checked properly.

### Expected behavior

All nodes matching any of the provided test conditions should be visited. If I specify `['heading', 'paragraph']`, both heading and paragraph nodes should be processed.

### Additional context

This seems to have started recently. Single condition checks work as expected, but multiple conditions via array skip the first test. The visitor appears to be starting from the wrong index when iterating through the test conditions.

---
Repository: /testbed
