# Bug Report

### Describe the bug

I'm getting a `ReferenceError` when using the AST visitor functionality. The code throws an error saying `resu is not defined` during tree traversal operations.

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

// This triggers the error
visitParents(tree, 'text', (node, parents) => {
  return [EXIT];
});
```

The error occurs when the visitor function returns an EXIT action during tree traversal. It seems like there's a reference to an undefined variable in the visit logic.

### Expected behavior

The tree traversal should complete successfully and exit cleanly when the visitor returns an EXIT action, without throwing a ReferenceError.

### System Info
- Node version: 18.x
- Browser: N/A (Node environment)

---
Repository: /testbed
