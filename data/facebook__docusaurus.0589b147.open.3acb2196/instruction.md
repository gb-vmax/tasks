# Bug Report

### Describe the bug
I'm experiencing an issue with MDX token handling where the `opener` function seems to be passing incorrect arguments to the `enter` callback. The second parameter to `enter.call()` should be the original token, but it appears to be receiving the created node instead.

### Reproduction
```js
// When processing MDX tokens
const token = {
  type: 'mdxJsxFlowElement',
  name: 'Component',
  // ... other token properties
}

// The opener function is called
// Expected: enter.call(this, createdNode, token)
// Actual: enter.call(this, createdNode, createdNode)
```

This causes issues when the `enter` callback tries to access properties from the original token, as it's receiving the created node object instead.

### Expected behavior
The `enter` callback should receive:
1. First argument: the newly created node
2. Second argument: the original token

This is important for maintaining proper token context during MDX compilation.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
