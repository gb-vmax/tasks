# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with MDX parsing where certain syntax constructs are not being handled correctly. The parser seems to be overwriting existing construct handlers instead of preserving them, which breaks the ability to use multiple syntax extensions together.

### Reproduction

```js
// When combining multiple syntax extensions that register handlers for the same code
const extension1 = {
  flow: {
    123: [handler1]
  }
}

const extension2 = {
  flow: {
    123: [handler2]
  }
}

// After merging, only the second handler is available
// Expected: both handlers should be preserved in an array
// Actual: the first handler is replaced with an empty object
```

### Expected behavior

When multiple syntax extensions register handlers for the same character code, they should be combined into an array of handlers rather than one replacing the other. The merged result should contain all handlers from both extensions.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This is causing syntax extensions to fail when used in combination, particularly affecting custom MDX components that rely on specific character codes.

---
Repository: /testbed
