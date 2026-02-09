# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where callbacks are being executed in the wrong order. When using custom handlers with the MDX compiler, the exit callback is being called before the custom `and` callback, which breaks the expected execution flow.

### Reproduction

```js
const mdx = require('@mdx-js/mdx');

let callOrder = [];

const options = {
  // Custom handler that tracks execution order
  handlers: {
    someNode: {
      exit: function(token) {
        callOrder.push('custom');
      }
    }
  }
};

// After compilation, the exit callback runs before the custom handler
// Expected order: ['custom', 'exit']
// Actual order: ['exit', 'custom']
```

### Expected behavior

Custom callbacks passed to the `closer` function should execute **before** the main exit callback, not after. This is important for proper cleanup and state management in custom handlers.

The execution order should be:
1. Custom `and` callback (if provided)
2. Main `exit2` callback

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken some of my custom MDX plugins that rely on the callback execution order. Any help would be appreciated!

---
Repository: /testbed
