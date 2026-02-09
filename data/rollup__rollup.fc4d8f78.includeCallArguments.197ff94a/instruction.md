# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where function call arguments are being included multiple times in the bundle. This seems to happen when a local variable is initialized with a function and that variable is called in multiple places.

### Reproduction

```js
function createLogger() {
  return function log(message) {
    console.log(message);
  };
}

const logger = createLogger();

// First call
logger('First message');

// Second call
logger('Second message');
```

When bundling code like this, the arguments from `createLogger()` appear to be processed incorrectly, leading to duplicate or unnecessary code being included in the output bundle.

### Expected behavior

Each function call's arguments should only be included once in the bundle, and the tree-shaking logic should properly track which arguments have already been processed to avoid redundant inclusions.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
