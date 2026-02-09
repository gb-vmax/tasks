# Bug Report

### Describe the bug

I'm experiencing a syntax error when running code that uses the `visitParents` function from the unist-util-remove-position vendor file. The code appears to be truncated or malformed, causing JavaScript parsing to fail.

### Reproduction

When trying to use functionality that relies on the `visitParents` function (such as AST traversal or position removal from syntax trees), the following error occurs:

```js
// Any code path that triggers visitParents will fail
// For example, processing markdown AST nodes:
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [{ type: 'text', value: 'Hello' }]
    }
  ]
};

// This will fail with a syntax error
visitParents(tree, 'text', (node, ancestors) => {
  console.log(node);
});
```

The JavaScript engine throws a parsing error because the return statement in the code seems incomplete.

### Expected behavior

The `visitParents` function should execute without syntax errors and properly traverse the AST tree, visiting nodes according to the specified test condition.

### System Info
- Node version: 18.x
- Browser: N/A (build-time error)

This looks like it might have been introduced during a recent code formatting or refactoring change. The function definition appears to be cut off mid-statement.

---
Repository: /testbed
