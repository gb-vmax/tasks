# Bug Report

### Describe the bug

I'm experiencing an issue where the AST visitor seems to be cutting off or not properly handling the result when traversing nodes. The visitor appears to be returning incomplete results during tree traversal, which causes unexpected behavior when processing syntax trees.

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
};

// Visitor function that should process all nodes
visitParents(tree, (node) => {
  console.log(node.type);
  // Expected to see: root, paragraph, text
  // But the traversal seems incomplete
});
```

### Expected behavior

The visitor should properly traverse all nodes in the tree and return complete results. All child nodes should be visited and the visitor should handle the EXIT case correctly without truncating the return value.

### System Info
- Node version: 18.x
- Package: unist-util-remove-position@5.0.0

---
Repository: /testbed
