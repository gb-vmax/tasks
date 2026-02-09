# Bug Report

### Describe the bug

The `removePosition` function is not properly removing position information from AST nodes. When called with default options, the position property remains on the nodes instead of being removed.

### Reproduction

```js
const tree = {
  type: 'root',
  position: {
    start: { line: 1, column: 1 },
    end: { line: 1, column: 10 }
  },
  children: [
    {
      type: 'text',
      value: 'hello',
      position: {
        start: { line: 1, column: 1 },
        end: { line: 1, column: 6 }
      }
    }
  ]
};

removePosition(tree);

// Position properties are still present
console.log(tree.position); // Should be undefined but isn't
console.log(tree.children[0].position); // Should be undefined but isn't
```

### Expected behavior

When `removePosition` is called without options (or with `force: false`), it should delete the `position` property from all nodes in the tree. The position information should be completely removed.

### Additional context

This seems to affect the default behavior of the function. The position data persists on nodes when it should be cleaned up.

---
Repository: /testbed
