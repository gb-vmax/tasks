# Bug Report

### Describe the bug

I'm experiencing an issue with the `unist-util-visit` utility where the visitor function doesn't seem to be checking all the test conditions properly. When passing multiple test functions to the visitor, some nodes that should match aren't being visited, and the behavior seems inconsistent.

### Reproduction

```js
const tests = [
  (node) => node.type === 'paragraph',
  (node) => node.type === 'heading',
  (node) => node.type === 'text'
];

visit(tree, tests, (node) => {
  console.log('Visiting:', node.type);
});
```

When running this, I notice that not all matching nodes are being visited. It seems like the first test condition is being skipped or some nodes that should match one of the tests aren't triggering the visitor callback.

### Expected behavior

All nodes matching any of the provided test functions should be visited. If a node matches any test in the array, the visitor callback should be called for that node.

### Additional context

This seems to have started happening recently. The visitor worked fine with multiple test conditions before. Not sure if this is related to a recent change in the codebase.

---
Repository: /testbed
